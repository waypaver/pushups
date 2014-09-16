from __future__ import absolute_import
import os, time
from celery import Celery
from django.conf import settings
from twilio.rest import TwilioRestClient
import datetime
import celery
from main.models import User, Workout
from celery.schedules import crontab
from celery.task import periodic_task
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pushups.settings')
app = Celery('pushups', include=['pushups.tasks'])
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.CELERYBEAT_SCHEDULE = {
    'sending-texts-task': {
        'task': 'pushups.celery.sendTexts',
        'schedule': crontab(day_of_week='1-5', hour='9-5', minute='0'),
        'args': (),
    },
    'closing-workouts-task': {
        'task': 'pushups.celery.closeWorkouts',
        'schedule': crontab(day_of_week='1-5', hour='9-5', minute='5'),
        'args': (),
    },
}

#import djcelery
#djcelery.setup_loader()

class Messenger:
	def __init__(self):
		self.accountSID = os.environ.get('TWILIO_ACCOUNT_SID')
		self.authenticationToken = os.environ.get('TWILIO_AUTH_TOKEN')
		self.twilioRestClient = TwilioRestClient(self.accountSID, self.authenticationToken)
	def sendMessage(self, recipientNumber, message):
		self.twilioRestClient.messages.create(to="+1" + str(recipientNumber), from_="+14234029660", body=message)

@app.task
def sendTexts():
	for user in User.objects.all():
		if user.active == True:
			newWorkout = Workout()
			newWorkout.participantID = user
			newWorkout.dateTimeStarted = datetime.datetime.now()
			newWorkout.save()
			messenger = Messenger()
			messenger.sendMessage(user.phoneNumber, user.firstName + ", time for pushups! In the next 5 minutes, text back how many pushups you did.")


@app.task
def closeWorkouts():
	for workout in Workout.objects.all():
		if workout.status == "pending":
			workout.status = "expired"
			workout.save()

if __name__ == '__main__':
	app.start()



