from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Schedule,Shopping_list,Stock,Stock_history,Food,Menu,Use_food,Recipe
from album.models import Image
from album.forms import ImageForm
from album.views import showall

# Create your views here.
def schedule(request, num=1):
    data = Schedule.objects.all()
    page = Paginator(data, 21)
    params = {
        'data': data,
        'data': page.get_page(num),
    }
    return render(request, 'foodmanager/schedule.html', params)

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
    menu_data = Use_food.objects.select_related('menu_CD').filter(menu_CD=num)

    foods_data = Use_food.objects.select_related('food_CD').filter(menu_CD=num)
    params = {
        'menu_data': menu_data,
        'foods_data': foods_data,
    }

    showall(request)

    return render(request, 'foodmanager/recipe.html', params)

def customize(request):
    return render(request, 'foodmanager/customize.html')
