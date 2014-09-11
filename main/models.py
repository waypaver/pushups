from django.db import models
from django.contrib import admin
from datetime import datetime
import os, time
#from django.core.validators import MinValueValidator, MaxValueValidator

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
	status = models.CharField(max_length=10,default="pending") #options: pending, completed, expired
	def __unicode__(self):
		return unicode(self.participantID.firstName + "'s " + self.status + " " + str(self.score) + "-pushup workout on "+ str(self.dateTimeStarted.strftime("%m/%d/%Y")) + " at " + str(self.dateTimeStarted.strftime("%H:%M")))

# class Schedule(models.Model):
# 	Monday = 0
# 	Tuesday = 1
# 	Wednesday = 2
# 	Thursday = 3
# 	Friday = 4
# 	Saturday = 5
# 	Sunday = 6
# 	AM = 0
# 	PM = 1
# 	DAY_CHOICES = (
# 		(Monday, 'Monday'),
# 		(Tuesday, 'Tuesday'),
# 		(Wednesday, 'Wednesday'),
# 		(Thursday, 'Thursday'),
# 		(Friday, 'Friday'),
# 		(Saturday, 'Saturday'),
# 		(Sunday, 'Sunday'),
# 	)
# 	DAYPART_CHOICES = (
# 		(AM, 'AM'),
# 		(PM, 'PM'),
# 	)
# 	day = models.IntegerField(choices=DAY_CHOICES, max_length=10)
# 	hour = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
# 	dayPart = models.IntegerField(choices=DAYPART_CHOICES, max_length=2)
# 	minute = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])

admin.site.register(User)
admin.site.register(Workout)
# admin.site.register(Schedule)