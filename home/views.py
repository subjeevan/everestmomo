from django.shortcuts import render
from .models import FoodMenu
# Create your views here.

def home(request):
    dish=FoodMenu.objects.all()
    return render(request,'home.html',{'dishes':dish})

