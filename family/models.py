from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from forms import BLOOD_GROUP_CHOICES
# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
BLOOD_GROUP_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+','AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),


)


VERIFICATION_QUESTION = (
    ('1', 'What is your pet name'),
    ('2', 'Your First School Name'),
    ('3', 'Your GirlFriend Name'),
    ('4', 'What is  your mother name'),



)
class UserInfo(models.Model):
    name = models.CharField(max_length=100,blank = False)
    sirname = models.CharField(max_length=100,blank = False)
    phone_no = models.CharField(max_length=10)
    age = models.IntegerField()
    dateofbirth = models.CharField(max_length=100,blank=False)
    Address = models.CharField(max_length=100,blank=True)
    bloodgroup = models.CharField(choices=BLOOD_GROUP_CHOICES,max_length=10)
    image = models.ImageField(blank = True)

class userVerificationModel(models.Model):
    username = models.CharField(max_length=100, blank=False)
    code = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)

    def __unicode__(self):
        return self.username







