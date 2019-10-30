from flask import Flask
from tasks import singleMethod
import os
from celery_app import celery_app
from celery.result import AsyncResult

TASK_ID = 0

flask_app = Flask(__name__)
@flask_app.route('/test', methods=['GET'])
def test():
	global TASK_ID
	if TASK_ID == 0:
		result = singleMethod.delay('P1bII', 'UniformGrid')
		TASK_ID = result.id
		return str(TASK_ID)
	else:
		result = AsyncResult(TASK_ID, app=celery_app)
		state = result.state
		if state == 'PENDING':
			return state
		else:
			return str(result.result)

if __name__ == '__main__':
	flask_app.run(host='0.0.0.0', port=4567, debug=True)
