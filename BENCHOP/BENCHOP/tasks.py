
from oct2py import Oct2Py
from celery_app import celery_app

@celery_app.task
def singleMethod(problem, method):	
	oc = Oct2Py()
	oc.chdir('/home/ubuntu/BENCHOPaaS/BENCHOP/BENCHOP')
	time, relerr = oc.feval('singleMethod', problem, method, nout=2)
	return  [time, relerr]
