from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import Schedule,Shopping_list,Stock,Stock_history,Food,Menu,Use_food,Recipe,Image
from .forms import ImageForm, StockForm


# Create your views here.
def schedule(request, num=1):
    #スケジュールを全件取得
    data = Schedule.objects.select_related('menu_CD').all()
    #日付で集約
    groupby_data = data.values('date').annotate(Count('date'))
    daylist = []                      #日付毎に朝昼夜のメニューを格納するリスト
    for val in groupby_data:
        menulist = ["", "", "", ""]   #日付、朝メニュー、昼メニュー、夜メニューの4枠に固定
        menulist[0] = val["date"]     #1つ目に日付を設定
        dayval = Schedule.objects.select_related('menu_CD').filter(date=val['date']).order_by('timing') #日付毎の朝昼夜メニューを取得
        for val2 in dayval:
            menu_dict = {val2.menu_CD_id: val2.menu_CD.menu_name}  #メニューのID(key)、メニュー名(value)をdictで取得
            menulist[int(val2.timing)] = menu_dict                 #リストの1番目：朝メニューのdict、2番目：昼メニューのdict、3番目：夜メニューのdict
        daylist.append(menulist)                                   #日付毎のメニューリストを戻り値のリストに収納

    page = Paginator(data, 7)
    menu_data = Menu.objects.select_related('picture').all()

    params = {
        'daylist': daylist,
        #'daylist': page.get_page(num),
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
    stocks = Stock.objects.select_related('food_CD').all().order_by('id')
    params = {
        'stocks': stocks,
        }
    return render(request, 'foodmanager/stock.html', params)        

def stock_edit(request, stock_id=None):
    """在庫の編集"""

    if stock_id:   # stock_id が指定されている (修正時)
        stock = get_object_or_404(Stock, pk=stock_id)
    else:         # stock_id が指定されていない (追加時)
        stock = Stock()

    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            stock = form.save(commit=False)
            stock.save()
            return redirect('foodmanager:stock')
    else:    # GET の時
        form = StockForm(instance=stock)  # stock インスタンスからフォームを作成

    return render(request, 'foodmanager/stock_edit.html', dict(form=form, stock_id=stock_id))


def stock_del(request, stock_id):
    """在庫の削除"""

    stock = get_object_or_404(Stock, pk=stock_id)
    stock.delete()
    return redirect('foodmanager:stock')

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


def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('foodmanager:schedule')
    else:
        form = ImageForm()

    context = {'form':form}
    return render(request, 'foodmanager/customize.html', context)