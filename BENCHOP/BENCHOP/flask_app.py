from flask import Flask, jsonify
from tasks import singleMethod
import os
from celery_app import celery_app
from celery.result import AsyncResult


PROBLEMS = ['P1aI', 'P1bI', 'P1cI', 'P1bII']
METHODS = ['COS']

ALL_RESULTS = {}

for prob in PROBLEMS:
	ALL_RESULTS[prob] = {}
	for method in METHODS:
		result = singleMethod.delay(prob, method)
		ALL_RESULTS[prob][method] = {'state': 'PENDING', 'id': result.id, 'result': ''}

flask_app = Flask(__name__)

@flask_app.route('/test', methods=['GET'])
def test():
	global ALL_RESULTS
	for prob in ALL_RESULTS.keys():
		for method in prob.keys():
			if method['state'] == 'PENDING':
				result = AsyncResult(method['id'], app=celery_app)
				if result.state != 'PENDING':
					method['state'] = result.state
					method['result'] = result.result
	return jsonify(ALL_RESULTS)

if __name__ == '__main__':
	flask_app.run(host='0.0.0.0', port=4567, debug=True)
