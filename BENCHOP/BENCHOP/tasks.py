from oct2py import Oct2Py #importing octave (as in examples) does not play with celery for some reason...
from celery_app import celery_app

@celery_app.task
def singleMethod(problem, method):	
	oc = Oct2Py()
	oc.chdir('/home/ubuntu/BENCHOPaaS/BENCHOP/BENCHOP')
	time, relerr = oc.feval('singleMethod', problem, method, nout=2)
	return  [time, relerr]

@celery_app.task
def singleMethodWithParams(problem, method, params):
	oc = Oct2Py()
	oc.chdir('/home/ubuntu/BENCHOPaaS/BENCHOP/BENCHOP')
	time, relerr = oc.feval('singleMethodWithParams', problem, method, params, nout=2)
	return [time, relerr]
