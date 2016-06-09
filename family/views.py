from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.shortcuts import redirect
# Create your views here.
from forms import familyform
from forms import testform,PhotoUploadForm
from models import UserInfo
from datetime import datetime


from django.core.mail import send_mail
import logging


def setdata(request):
    print "In this"
    if request.method == "GET":
        family_form = familyform()
        return render(request, 'family_setdata.html', {
            'form': family_form})

    if request.method == "POST":
        form = familyform(request.POST)
        print form.errors
        if form.is_valid():
            dateofbirth = form.cleaned_data['date_of_birth']
            b_date = datetime.strptime(dateofbirth, '%m/%d/%Y')
            age = ((datetime.today() - b_date).days / 365)

            if UserInfo.objects.filter(name=form.cleaned_data['name'],date_of_birth = form.cleaned_data['date_of_birth']).exists():
                return HttpResponse("Data is already saved for this user")

            f_info = UserInfo(name=form.cleaned_data['name'],
                              last_name=form.cleaned_data['last_name'],
                              age=age,
                              father_name =form.cleaned_data['father_name'],
                              phone_no=form.cleaned_data['phone_no'],
                              date_of_birth=form.cleaned_data['date_of_birth'],
                              Address=form.cleaned_data['Address'],
                              blood_group=form.cleaned_data['blood_group'],
                              image=form.cleaned_data['image']
                              )

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

def aboutus(response):
    return HttpResponse("About Us working")

def contact(request):
    return render_to_response("contact.html")

def photo_upload_view(request):

    if request.method == 'POST':
        print "In thish"
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Done')
    else:
        form = PhotoUploadForm()

    submit_btn = "Upload Post"

    context = {
        "form": form,
        "submit_btn": submit_btn
    }
    return render(request, "photo_upload.html", context)