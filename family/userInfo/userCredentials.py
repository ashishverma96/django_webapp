from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
# Create your views here.

from django.shortcuts import redirect


import random

from ..models import UserInfo
from ..models import userVerificationModel


from ..forms import UserSignUpform
from ..forms import loginform
from ..forms import verificationform


import logging
logger = logging.getLogger('loggly_logs')
logger1 = logging.getLogger('django_logs')


def signup(request):
    if request.method == "GET":
        reg_form = verificationform()
        return render(request, 'userregister.html',{
            'form': reg_form})

    if request.method == "POST":
        form = UserSignUpform(request.POST)
        if form.is_valid():
            try:
                user_code = userVerificationModel.objects.get(code=form.cleaned_data['code'])
                email =form.cleaned_data['email_id']
                if (email == user_code.email and user_code):
                    username = user_code.username
                    if User.objects.filter(username=username).exists():
                        return HttpResponse("Username already exist")
                    if (form.cleaned_data['password']!= form.cleaned_data['confirm_password']):
                        return HttpResponse("Password Does not match")
                    else:
                        user = User.objects.create_user(username=username, email=email \
                                                            , password=form.cleaned_data['password'])
                        return render(request, 'login.html')
            except:
                return HttpResponse("Incorrect Code")
        else:
            HttpResponse("Please fill all fields")



def register(request):
    if request.method == "GET":
        reg_form = verificationform()
        return render(request, 'userregister.html', {
            'form': reg_form})

    if request.method == "POST":
        reg_form = verificationform(request.POST)
        if reg_form.is_valid():
            try:
                user_present = User.objects.get(username=reg_form.cleaned_data['username'])
                if user_present:
                    return HttpResponse('User Already Present', status=200)
            except:
                verification_code = random.randint(0, 9999)
                userVerificationModel.objects.create(username=reg_form.cleaned_data['username'],
                                                     code=verification_code,
                                                     email=reg_form.cleaned_data['email_id'])
                email_body = 'Verification Code :  %s' % verification_code
                mail = send_mail('Account Varification Mail', email_body, 'akumarlpu@gmail.com',
                                 [
                                     reg_form.cleaned_data['email_id']])

                signupform = UserSignUpform()
                return render(request, 'signup.html', {
                    'form': signupform})

    """
    def post(self,request):
        if self.reg_form.is_valid():
            try:
                user_present = User.objects.get(username=self.reg_form.cleaned_data['username'])
                if user_present:
                    return HttpResponse('User Already Present', status=200)
            except:
                verification_code = random.randint(0, 9999)
                userVerificationModel.objects.create(username=self.reg_form.cleaned_data['username'], code=verification_code,
                                                     email=self.reg_form.cleaned_data['email_id'])
                email_body = 'Verification Code :  %s' % verification_code
                mail = send_mail('Account Varification Mail', email_body, 'akumarlpu@gmail.com',
                                 [self.reg_form.cleaned_data['email_id']])

                signupform = UserSignUpform()
                return render(request, 'signup.html', {
                    'form': signupform})
    """

def login(request):
    if request.method == "GET":
        login_form = loginform()
        return render(request, 'login.html', {
            'form': login_form})

    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            for i in User.objects.all():
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                if user:
                    return render(request,"familyMainPage.html")
                else:

                    return HttpResponse(status=501)

        else:
            print "form Invalid"

def check_username_available(request):
    return HttpResponse(False)
