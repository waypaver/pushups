from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from twilio.rest import TwilioRestClient
import datetime
import celery
from main.models import User, Workout

#osascript -e 'tell application "Terminal" to activate' -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down'
#export DJANGO_SETTINGS_MODULE='pushups.settings'
#export REDIS_URL='redis://'
#redis-server
#celery -A pushups worker -l info
#celery -A pushups beat

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pushups.settings')
app = Celery('pushups', include=['pushups.tasks'])
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

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
	messenger.sendMessage(4235673625, "Feel the Celery beat!")

if __name__ == '__main__':
	app.start()





# messenger = Messenger()
# for user in User.objects.all():
	# if user.active == True:
		# messenger.sendMessage(user.phoneNumber, "Hello " + user.firstName)	





