from flask import Flask, jsonify
from tasks import singleMethod
from celery_app import celery_app
from celery.result import AsyncResult

#PROBLEMS = ['P1aI', 'P1bI', 'P1cI', 'P1aII', 'P1bII', 'P1cII']
#METHODS = ['COS', 'RBFFD', 'UniformGrid']

#Use only a subset of problems and a single method for testing.
PROBLEMS = ['P1aI', 'P1bI', 'P1cI', 'P1aII', 'P1bII']
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
		ALL_RESULTS[prob][method] = {'state': 'PENDING', 'id': result.id, 'result': {}}

#Start the flask app after all tasks are created
flask_app = Flask(__name__)

#Updates global variable with newly finished results and returns everything
@flask_app.route('/test', methods=['GET'])
def test():
	global ALL_RESULTS
	for prob in ALL_RESULTS.keys():
		for method in ALL_RESULTS[prob].keys():
			if ALL_RESULTS[prob][method]['state'] == 'PENDING':
				result = AsyncResult(ALL_RESULTS[prob][method]['id'], app=celery_app)
				if result.state == 'SUCCESS':
					ALL_RESULTS[prob][method]['state'] = result.state
					ALL_RESULTS[prob][method]['result']['time'] = result.result[0]
					ALL_RESULTS[prob][method]['result']['relerr'] = result.result[1]
	return jsonify(ALL_RESULTS)

if __name__ == '__main__':
	flask_app.run(host='0.0.0.0', port=4567, debug=True)
