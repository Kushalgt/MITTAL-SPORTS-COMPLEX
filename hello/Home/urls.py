from django.contrib import admin
from django.urls import path
from Home import views
#from login.views import swimming
urlpatterns = [
    path("",views.index,name="home"),
    path("registration",views.registration,name="registration"),
]
