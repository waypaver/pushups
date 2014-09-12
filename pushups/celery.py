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

#DON'T FORGET TO RUN POSTGRESQL APP!!!
#export DJANGO_SETTINGS_MODULE='pushups.settings'
#export REDIS_URL='redis://'
#redis-server
#celery -A pushups worker -l info
#celery -A pushups beat

#ps aux | grep -i manage
#kill -9 pid

#osascript -e 'tell application "Terminal" to activate' -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down'


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pushups.settings')
app = Celery('pushups', include=['pushups.tasks'])
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.CELERYBEAT_SCHEDULE = {
    'sending-texts-task': {
        'task': 'pushups.celery.sendTexts',
        'schedule': crontab(day_of_week='1-5', hour='9-5', minute='0,4,8,12,16,20,24,28,32,36,40,44,48,52,56'),
        'args': (),
    },
    'closing-workouts-task': {
        'task': 'pushups.celery.closeWorkouts',
        'schedule': crontab(day_of_week='1-5', hour='9-5', minute='2,6,10,14,18,22,26,30,34,38,42,46,50,54,58'),
        'args': (),
    },
}

import djcelery
djcelery.setup_loader()


class Messenger:
	def __init__(self):
		self.accountSID = "ACb0757d158c432cbd06f53e228a9693a9"
		self.authenticationToken = "6bef01d2def1978f9d2bea7c15aa8a17"
		self.twilioRestClient = TwilioRestClient(self.accountSID, self.authenticationToken)
	def sendMessage(self, recipientNumber, message):
		self.twilioRestClient.messages.create(to="+1" + str(recipientNumber), from_="+14234029660", body=message)

@app.task
def test_sms():
	messenger = Messenger()
	messenger.sendMessage(8143302929, "Feel the Celery beat!")

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



