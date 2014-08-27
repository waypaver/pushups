from django.db import models
from django.contrib import admin

class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_address = models.CharField(max_length=100)
	phone_number = models.IntegerField(default=0)
	score = models.IntegerField(default=0)
	def __unicode__(self):
		return unicode(self.first_name + " " + self.last_name)

class Twilio(models.Model):
	SID = models.CharField(max_length=100)
	auth_token = models.CharField(max_length=100)

admin.site.register(User)
admin.site.register(Twilio)

