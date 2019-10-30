from flask import Flask
from moretasks import benchmark
import os
from celery import Celery, group

env = os.environ
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL', 'amqp://guest@localhost//')
CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND', 'amqp://')

celery = Celery('tasks', broker = CELERY_BROKER_URL, backend = CELERY_RESULT_BACKEND)

flask_app = Flask(__name__)
@flask_app.route('/test', methods=['GET'])
def test():
	results = benchmark.delay()
	return str(results.get())

if __name__ == '__main__':
	flask_app.run(host='0.0.0.0', port=4567, debug=True)
