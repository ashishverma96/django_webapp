from django import forms
from models import UserInfo
from models import userVerificationModel
from django.shortcuts import render_to_response
from django.http import HttpResponse

ACCOUNT_CHOICES = (
    ('family', 'Family'),
    ('university', 'University'),
    ('school', 'School'),
)

BLOOD_GROUP_CHOICES = (
    ('1', 'A+'),
    ('2', 'A-'),
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



class familyform(forms.Form):
    #class Meta:
    #    model = FamilyInfo

    #    fields = ['name','phone_no','age','image']
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_no = forms.CharField(required=True)

    dateofbirth = forms.CharField(max_length=100, required=True,label="Date of Birth")
    Address = forms.CharField(max_length=100, required=False)
    bloodgroup = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES,required=True)
    image = forms.ImageField(required=False)


class UserSignUpform(forms.Form):
    code = forms.IntegerField(required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput,required=True)
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput,required=True)
    email_id = forms.EmailField(required=True)



class loginform(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)


class verificationform(forms.Form):
    username = forms.CharField(required=True)
    email_id = forms.EmailField(required=True)


class testform(forms.Form):
    bloodgroup = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES, required=True)
