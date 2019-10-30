from flask import Flask
from tasks import benchmark
import os
from celery import Celery

flask_app = Flask(__name__)
@flask_app.route('/test', methods=['GET'])
def test():
	results = benchmark.delay()
	return str(results.get())

if __name__ == '__main__':
	flask_app.run(host='0.0.0.0', port=4567, debug=True)
