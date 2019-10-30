from celery import Celery 
from oct2py import Oct2Py
import os

env = os.environ
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL', 'amqp://guest@localhost//')
CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND', 'amqp://')

#app = Celery('tasks', broker= CELERY_BROKER_URL, backend = CELERY_RESULT_BACKEND)
app = Celery('tasks', backend='rpc://', broker='pyamqp://')

#os.chdir('/home/ubuntu/BENCHOPaaS/BENCHOP/BENCHOP')
@app.task
def benchmark():	
	oc = Oct2Py()
	oc.chdir('/home/ubuntu/BENCHOPaaS/BENCHOP/BENCHOP')
	time, relerr = oc.feval('singleMethod', 'P1aI', 'COS', nout=2)
	return  [time, relerr]
