from flask import Flask, jsonify, render_template, request
from tasks import singleMethod, singleMethodWithParams
from celery_app import celery_app
from celery.result import AsyncResult

import pygal, json
from pygal.style import Style
from pygal.style import CleanStyle, DefaultStyle

'''
All problems and methods

PROBLEMS = ['P1aI', 'P1bI', 'P1cI', 'P1aII', 'P1bII', 'P1cII']
METHODS = ['COS', 'RBFFD', 'UniformGrid']

RBFFD method is useless since it doesn't work and always returns NaN values.

'''


#Use only a subset of problems and a single method for testing.
PROBLEMS = ['P1aI', 'P1bI', 'P1cI']
METHODS = ['COS']  

'''
The goal here is to start the benchmark with default parameters only once, 
and then the user can obtain all the results that are ready.

To achieve this the flask app starts all the celery tasks on startup and 
keeps track of state in a global variable. Obviously not ideal but it 
works for basic testing.
'''

#Start benchmarking tasks
ALL_RESULTS = {}
for prob in PROBLEMS:
	ALL_RESULTS[prob] = {}
	for method in METHODS:
		result = singleMethod.delay(prob, method)
		ALL_RESULTS[prob][method] = {'state': 'PENDING', 'id': result.id, 'result': {'time': 0, 'relerr': 0}}

#Use this to update state
def update_results():
	global ALL_RESULTS
	for prob in ALL_RESULTS.keys():
		for method in ALL_RESULTS[prob].keys():
			if ALL_RESULTS[prob][method]['state'] == 'PENDING':
				result = AsyncResult(ALL_RESULTS[prob][method]['id'], app=celery_app)
				if result.state == 'SUCCESS':
					ALL_RESULTS[prob][method]['state'] = result.state
					ALL_RESULTS[prob][method]['result']['time'] = result.result[0]
					ALL_RESULTS[prob][method]['result']['relerr'] = result.result[1]

#Start the flask app after all tasks are created
flask_app = Flask(__name__)

#Updates global variable with newly finished results and returns everything
@flask_app.route('/benchmark', methods=['GET'])
def obtain_benchmark_results():
	
	update_results()

	global ALL_RESULTS
	time_charts = []
	relerr_charts = []
	for prob in sorted(ALL_RESULTS.keys()):
		time_chart = pygal.Bar(style=CleanStyle)
		time_chart.title = "Time to solve problem: " + prob
		time_chart.y_title = "Execution time [s]"

		relerr_chart = pygal.Bar(style=DefaultStyle)
		relerr_chart.title = "Relative error for problem: " + prob
		relerr_chart.y_title = "Relative error"

		labels = []
		time_data = []
		relerr_data = []
		for method in ALL_RESULTS[prob].keys():
			if ALL_RESULTS[prob][method]['state'] == 'SUCCESS':
				labels.append(method)
			else:
				labels.append(method + " PENDING")

			time_data.append(ALL_RESULTS[prob][method]['result']['time'])
			relerr_data.append(ALL_RESULTS[prob][method]['result']['relerr'])

		time_chart.x_labels = map(str, labels)
		time_chart.add('Time', time_data)
		time_chart_data = time_chart.render_data_uri()
		time_charts.append(time_chart_data)

		relerr_chart.x_labels = map(str, labels)
		relerr_chart.add('Relerr', relerr_data)
		relerr_chart_data = relerr_chart.render_data_uri()
		relerr_charts.append(relerr_chart_data)
		
	return render_template("webui.html", results = ALL_RESULTS, time_charts = time_charts, relerr_charts = relerr_charts)


@flask_app.route('/benchmark/json', methods=['GET'])
def obtain_results_json():
	global ALL_RESULTS
	update_results()
	return jsonify(ALL_RESULTS)

@flask_app.route('/UDF', methods=['POST'])
def UDF():
	global ALL_RESULTS
	try:
		user_variables = request.get_json()
		prob = user_variables['problem']
		method = user_variables['method']
		params = user_variables['params']
		result = singleMethodWithParams.delay(prob, method, params).get()
		update_results()
		comparison = {'standard_results': ALL_RESULTS, 'UDF': {'time': result[0], 'relerr': result[1]}}
		return jsonify(comparison)
	except:
		return str('wrong content, use: {"problem": "prob", "method": "method", "params": [S, K, T, r, sig]}\n') 



if __name__ == '__main__':
	flask_app.run(host='0.0.0.0', port=4567, debug=True)
