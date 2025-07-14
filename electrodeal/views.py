
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request,"index.html")

def register(request):
    form=UserCreationForm()
    context={
        "form":form
    }
    return render(request,"register.html",context)

def login(request):
    context={}
    return render(request,"login.html",context)

def about(request):
    context={}
    return render(request,"about.html",context)

def contact(request):
    context={}
    return render(request,"contact.html",context)