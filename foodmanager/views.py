from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Schedule,Shopping_list,Stock,Stock_history,Food,Menu,Use_food,Recipe

# Create your views here.
def top(request):
    return render(request, 'foodmanager/top.html')

def schedule(request):
    return render(request, 'foodmanager/schedule.html')

def menu(request):
    data = Menu.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'foodmanager/menu.html', params)

def stock(request):
    return render(request, 'foodmanager/stock.html')

def shopping_list(request):
    return render(request, 'foodmanager/shopping_list.html')

def recipe(request,num):

    return render(request, 'foodmanager/recipe.html')

def customize(request):
    return render(request, 'foodmanager/customize.html')
