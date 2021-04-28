from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Schedule,Shopping_list,Stock,Stock_history,Food,Menu,Use_food,Recipe,Image
from .forms import ImageForm

# Create your views here.
def schedule(request, num=1):
    data = Schedule.objects.all()
    page = Paginator(data, 21)
    menu_data = Menu.objects.select_related('picture').all()
    params = {
        'data': data,
        'data': page.get_page(num),
        'menu_data': menu_data
    }
    return render(request, 'foodmanager/schedule.html', params)

def menu(request):
    data = Menu.objects.select_related('picture').all()
    params = {
        'data': data,
    }
    return render(request, 'foodmanager/menu.html', params)

def stock(request):
    return render(request, 'foodmanager/stock.html')

def shopping_list(request):
    return render(request, 'foodmanager/shopping_list.html')

def recipe(request,num):
    menu_data = Menu.objects.select_related('picture').filter(menu_CD=num)
    foods_data = Use_food.objects.select_related('food_CD').filter(menu_CD=num)
    data = Recipe.objects.all().filter(menu_CD=num)

    params = {
        'menu_data': menu_data,
        'foods_data': foods_data,
        'data': data
    }
    
    return render(request, 'foodmanager/recipe.html', params)

def customize(request):
    return render(request, 'foodmanager/customize.html')

def showimage(request, num):
    image = Image.objects.filter(menu_CD=num)
    context = {'image':image}
    return render(request, 'foodmanager/menu.html', context)

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('foodmanager:menu')
    else:
        form = ImageForm()

    context = {'form':form}
    return render(request, 'foodmanager/customize.html', context)