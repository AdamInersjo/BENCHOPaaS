from celery import Celery 
from oct2py import Oct2Py

app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
def benchmark():	
	oc = Oct2Py()
	oc.chdir('/home/ubuntu/BENCHOPaaS/BENCHOP/BENCHOP')
	time, relerr = oc.feval('singleMethod', 'P1aI', 'COS', nout=2)
	return  [time, relerr]
