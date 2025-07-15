
from django.shortcuts import render
from .forms import CustomUserCreationForm

def home(request):
    return render(request,"index.html")

def register(request):
    if request.method=="GET":
        form=CustomUserCreationForm()
        context={
            "form":form
        }
        return render(request,"register.html",context)
    elif request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"register.html")

       


def login(request):
    context={}
    return render(request,"login.html",context)

def about(request):
    context={}
    return render(request,"about.html",context)

def contact(request):
    context={}
    return render(request,"contact.html",context)