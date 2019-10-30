#Not sure about best practice regarding the celery_app, but this seems to work for now.

from celery import Celery 
celery_app = Celery('tasks', backend='rpc://', broker='pyamqp://')