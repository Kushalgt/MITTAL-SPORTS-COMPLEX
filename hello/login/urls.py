from django.contrib import admin
from django.urls import path,include
from login import views



urlpatterns = [
    path("",views.login,name="login"),
    #path("xyz",views.login,name="login2"),
    ]