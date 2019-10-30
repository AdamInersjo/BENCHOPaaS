from flask import Flask
from tasks import singleMethod
import os
from celery_app import celery_app
from celery.result import AsyncResult

flask_app = Flask(__name__)
@flask_app.route('/test', methods=['GET'])
def test():
	results = singleMethod.delay('P1aI', 'COS')
	return str(results.get())

if __name__ == '__main__':
	flask_app.run(host='0.0.0.0', port=4567, debug=True)
