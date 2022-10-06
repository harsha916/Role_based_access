from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signIn/',views.signin,name="signIn"),
    path('signUp/',views.signup,name="signUp"),
    path('signOut/',views.signout,name="signOut"),
    #path('customer/',views.customer,name="customer"),
    #path('service_provider',views.service_provider,name="service_provider"),
]
