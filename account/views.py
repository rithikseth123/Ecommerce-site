from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.


def register(request):
    if request.method =="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=True
            user.save()
            return redirect("/")
        else:
            return render(request,"account/register.html",{"form":form})
    form =NewUserForm()
    return render (request,"account/register.html",{"form":form})
    
def login(request):
    if request.method=="POST":
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            u=request.POST["username"]
            p=request.POST["password"]
            user=authenticate(request,username=u,password=p)
            if user is not None:
                auth_login(request,user)
                return redirect("/")
            else:
                print("No Valid")
    form=AuthenticationForm()
    return render(request,"account/login.html",{"form":form})
ok
def logout(request):
    auth_logout(request)
    return redirect("/")