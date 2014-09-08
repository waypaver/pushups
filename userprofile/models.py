from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  phone_number = PhoneNumberField(blank=False)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
