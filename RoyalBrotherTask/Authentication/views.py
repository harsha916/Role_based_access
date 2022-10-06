from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def home(request):
    return render(request,"index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        add_grp = request.POST['groups']
        my_group = Group.objects.get(name=add_grp) 
        myuser = User.objects.create_user(username=username,password=password)
        myuser.email = email
        myuser.save()
        myuser.groups.add(my_group) 

        messages.success(request,"Your account has been created")

        return redirect('signIn')
    return render(request,"signUp.html")

def signin(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user) 
            return render(request,'index.html',{'name':username})

        else:
            messages.error(request, "Wrong creditials")
            return render(request,"index.html")
    return render(request,"signIn.html")

def signout(request):
    logout(request)
    return redirect('home')