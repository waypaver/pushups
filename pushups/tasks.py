from __future__ import absolute_import

from pushups.celery import app

@app.task
def add(x, y):
	return x + y

@app.task
def hello():
	return "Hello World"