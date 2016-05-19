from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')
import time

@app.task
def print_hello():
    while(1):
        print '*********'
        localtime = time.asctime(time.localtime(time.time()))
        print "TIme is  Celery is ",localtime
        print '*****$$****'
