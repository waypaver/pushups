from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User
import os, time

# class UserProfile(models.Model):
# 	user = models.OneToOneField(User)

# 	phoneNumber = models.CharField(max_length=10,default="")

# class Workout(models.Model):
# 	participantID = models.ForeignKey(User)
# 	dateTimeStarted = models.DateTimeField(auto_now_add=True)
# 	score = models.IntegerField(default=0)
# 	status = models.CharField(max_length=10,default="pending") #options: pending, completed, expired
# 	def __unicode__(self):
# 		return unicode(self.participantID.firstName + "'s " + self.status + " " + str(self.score) + "-pushup workout on "+ str(self.dateTimeStarted.strftime("%m/%d/%Y")) + " at " + str(self.dateTimeStarted.strftime("%H:%M")))

# admin.site.register(UserProfile)
# admin.site.register(Workout)