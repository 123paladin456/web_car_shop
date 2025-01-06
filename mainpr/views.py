from django.shortcuts import render,get_object_or_404
from mainpr.models import *
# Create your views here.
def home(request):
    cars = Car.objects.all()
    brands = Brend.objects.all()
    return render(request, 'index.html', {"all_cars":cars, "all_brends":brands})
def detail(request, now_car):
    model_name = get_object_or_404(klass=Model, name=now_car)
    car_now = get_object_or_404(klass=Car, model=model_name)
    return render(request, 'detail.html', {'car': car_now})
def category(request, brand_id):
    brend_object = get_object_or_404(klass=Brend, id=brand_id)
    brends = Car.objects.filter(brend=brend_object)
    cars = Car.objects.all()
    return render(request, 'category.html', {'brends': brends, "all_cars":cars})
