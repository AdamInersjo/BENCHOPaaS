from tasks import singleMethod
from celery_app import celery_app
from celery.result import AsyncResult
import time

#NOT TESTED (could not connect to my vms...)

#A test to verify that adding more workers speeds up evaluation of the benchmark.

#Since this essentially is what the flask app does, running this with different numbers
# of workers would indicate that the service scales.

start = time.time()

PROBLEMS = ['P1aI', 'P1bI', 'P1cI', 'P1aII']
METHODS = ['COS', 'UniformGrid']

print('Sending tasks')
ALL_RESULTS = {}
for prob in PROBLEMS:
	ALL_RESULTS[prob] = {}
	for method in METHODS:
		result = singleMethod.delay(prob, method)
		ALL_RESULTS[prob][method] = {'state': 'PENDING', 'id': result.id, 'result': {'time': 0, 'relerr': 0}}

print('Tasks sent')
while not update_results():
    print('working...')
    time.sleep(1)
finish = time.time()
print('Done!')
print('Total time elapsed: ', finish-start)

def update_results():
	global ALL_RESULTS
    done = True
	for prob in ALL_RESULTS.keys():
		for method in ALL_RESULTS[prob].keys():
			if ALL_RESULTS[prob][method]['state'] == 'PENDING':
                done = False
				result = AsyncResult(ALL_RESULTS[prob][method]['id'], app=celery_app)
				if result.state == 'SUCCESS':
					ALL_RESULTS[prob][method]['state'] = result.state
					ALL_RESULTS[prob][method]['result']['time'] = result.result[0]
					ALL_RESULTS[prob][method]['result']['relerr'] = result.result[1]
    return done