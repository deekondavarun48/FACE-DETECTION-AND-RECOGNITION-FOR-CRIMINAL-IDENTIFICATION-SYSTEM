from django.shortcuts import render,redirect
from django.contrib import messages

from adminapp.models import PoliceOfficerModel

# Create your views here.
# home views here.
def home_index(request):
    return render(request,"home/home-index.html")






def home_about(request):
    return render(request,"home/home-about.html")

def home_contact(request):
    return render(request,"home/home-contact.html")

