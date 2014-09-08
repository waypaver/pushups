from django.db import models
from django.contrib import admin
from datetime import datetime

class User(models.Model):
	phoneNumber = models.CharField(max_length=10,default="")
	emailAddress = models.CharField(max_length=100,default="")
	firstName = models.CharField(max_length=30,default="")
	lastName = models.CharField(max_length=30,default="")
	active = models.BooleanField(default=False)

	def __unicode__(self):
		return unicode(self.firstName + " " + self.lastName)

class Workout(models.Model):
	participantID = models.ForeignKey(User)
	dateTimeStarted = models.DateTimeField(auto_now_add=True)
	score = models.IntegerField(default=0)
	status = models.CharField(max_length=10,default="pending")

admin.site.register(User)
admin.site.register(Workout)