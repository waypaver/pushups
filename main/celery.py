from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from twilio.rest import TwilioRestClient
import datetime
import celery
#from main.models import User, Workout

#celery -A pushups worker -l info

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pushups.settings')
app = Celery('pushups')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

class Messager:
	def __init__(self):
		self.accountSID = "ACb0757d158c432cbd06f53e228a9693a9"
		self.authenticationToken = "6bef01d2def1978f9d2bea7c15aa8a17"
		self.twilioRestClient = TwilioRestClient(self.accountSID, self.authenticationToken)
	def sendMessage(self, recipientNumber, message):
		self.twilioRestClient.messages.create(to="+1" + str(recipientNumber), from_="+14234029660", body=message)

# messenger = Messager()
# for user in User.objects.all():
	# if user.active == True:
		# messenger.sendMessage(4235673625, "Hello: " + user.firstName)	








