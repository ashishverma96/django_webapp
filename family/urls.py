__author__ = 'ashish'


from django.conf.urls import url,include
from django.contrib import admin
from views import *
from userInfo import userCredentials
from password_reset import password
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import password_reset
from django.views.generic import TemplateView




urlpatterns = [
    url(r'^setdata', setdata, name='setdata'),
    url(r'^getdata', getdata, name='getData'),
    url(r'^signup', userCredentials.signup, name='userSignup'),
    url(r'^check_username', userCredentials.check_username_available, name='check_username'),

    url(r'^register', userCredentials.register, name='register'),
    url(r'^aboutus', aboutus, name='aboutus'),
    url(r'^contact', contact, name='contact'),
    url(r'^photo', photo_upload_view, name='photo'),



    ##URL for Passwords
    url(r'^user/password/reset/$',
        password.password_reset,
        {'post_reset_redirect': 'userLogin'},
        name="password_reset"),

    url(r'^user/password/reset/done/$',
     userCredentials.login,name='userLogin'),

    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
     'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect': 'userLogin'},
        name="password_reset"),

    url(r'^user/password/done/',
        userCredentials.login, name='userLogin'),

     url(r'^', userCredentials.login, name='userLogin'),


]

#urlpatterns += staticfiles_urlpatterns()