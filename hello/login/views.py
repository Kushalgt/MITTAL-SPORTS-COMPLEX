from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from http.client import HTTPResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from Home.models import Contact

from Home.views import index

# Create your views here.


def login(request):
    #print("enter email:")
    #email=input()
    #password=input()
    if  request.method=="POST":
      email=request.POST.get('email')
      password=request.POST.get('password')
      user = authenticate(username=email, email=password)
      if user is not None:
        return render(request,'sports.html')
      else:
        return HTTPResponse("LOGIN CREDENTIALS DIDNOT MATCHED")

    return render(request,'loginindex.html')


