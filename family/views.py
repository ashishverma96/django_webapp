from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.shortcuts import redirect
# Create your views here.
from forms import familyform
from forms import testform
from models import UserInfo
from django.core.mail import send_mail
import logging
logger = logging.getLogger('loggly_logs')
logger.info('Hi, Welcome to Loggly.')

@login_required
def setdata(request):
    if request.method == "GET":
        family_form = familyform()
        return render(request, 'family_setData.html', {
            'form': family_form})

    if request.method == "POST":
        print "In SET DAATA"
        form = familyform(request.POST)
        form.errors
        if form.is_valid():
            print "Form is valid"
            f_info = UserInfo(name=form.cleaned_data['name'], age=form.cleaned_data['age'],
                              phone_no=form.cleaned_data['phone_no'])
            f_info.save()
            return HttpResponse("Data Entered successfully")
        else:
            print "Data is not entered"
            return HttpResponse("Please provide Correct data")



def home(request):
    response = render(request, "signup.html")
    return response

def not_found(request):
    response = render(request, "404.html")
    response.status_code = 404
    return response


def main_page(request):
    return render_to_response("familyMainPage.html")

@login_required
def getdata(request):
    test_form = testform()
    print "uyhja"
    return render(request, 'family_get.html', {'form': test_form})

    #if request.method == "GET":
    #    test_form = testform()
       # return render(request, 'family_get.html',{'form': test_form})

    if request.method == "POST":
        print "re",request.POST

        if request.POST['val'] == "1":
            return redirect('https://www.loggly.com/docs/logging-setup/')
        if request.POST['val'] == "2":
            return redirect('https://www.loggly.com/docs/loggly-5-minutes/')
        if request.POST['val'] == "3":
            return redirect('https://www.loggly.com/log-management-explained/')

        if request.POST['val'] == "4":

            email_body = 'Comment  :  %s' % request.POST['comment']
            email_subject = "loggly Account Deletion"
            mail = send_mail(email_subject, email_body, 'akumarlpu@gmail.com',
                             ['ashishk.verma76@gmail.com'])

        #    return redirect('https://www.loggly.com/docs/loggly-5-minutes/')

            return redirect('https://www.loggly.com')
        #x = UserInfo.objects.get(name = request.POST['name'])
        #print x


def ns(request):
    return HttpResponse("AA gata")

def aboutus(response):
    return HttpResponse("About Us working")

def contact(request):
    return render_to_response("contact.html")