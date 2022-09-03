import email
from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib.auth.models import User
# context is set of variables
context={
    "variable":"this is sent"
}

# Create your views here.
def index(request):

    return render(request,'index.html',context)


def registration(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        username=request.POST.get('username')
       # user = User.objects.create_user(email,password,username)
        #user.save
        contact=Contact(email=email,password=password,username=username,slotsbooked='0')
        contact.save()
    return render(request,'registration.html')

