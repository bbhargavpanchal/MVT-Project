from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import details

# Create your views here.
def homes(response): 
    return render(response, "home/main.html",{})

def output(response):
    f=details.objects
    if response.POST.get("submit") =="submit":
        name=response.POST.get("name")
        email=response.POST.get("email")
        contact=response.POST.get("contact")
        f.create(name=name, email=email, contact=contact)
        f.get(name=name).save()
    return render(response, "home/details.html",{"f":f})