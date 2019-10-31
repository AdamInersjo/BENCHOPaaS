#Replace backend = broker with appropriate values 

from celery import Celery 
celery_app = Celery('tasks', backend='rpc://', broker='pyamqp://')