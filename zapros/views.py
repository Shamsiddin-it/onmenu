from django.shortcuts import render
from .models import Dish

def menu_view(request):
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {'dishes': dishes})

