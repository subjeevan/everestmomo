from django.shortcuts import render,redirect
from django.contrib import messages
from .models import FoodMenu,Contact,Review,Orgainfo
from .forms import FoodMenuForm,ContactForm,ReviewForm,OrgainfoForm
# Create your views here.

def home(request):
    if request.method=='POST':
        contactform=ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            messages.success(request,'Data Saved Successfully')
            return redirect('home')
        else:
            messages.error(request,"Kindly provide valid informations")
    return render(request,'home.html')