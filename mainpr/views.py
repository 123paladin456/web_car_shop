from django.shortcuts import render
from mainpr.models import *
# Create your views here.
def home(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {"all_cars":cars})