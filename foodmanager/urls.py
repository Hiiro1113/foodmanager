from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule, name="schedule"),
    path('<int:num>', views.schedule, name="schedule"),
    path('menu', views.menu, name="menu"),
    path('stock', views.stock, name="stock"),
    path('stock/add/', views.stock_edit, name='stock_add'),  # 登録
    path('stock/mod/<int:stock_id>/', views.stock_edit, name='stock_mod'),  # 修正
    path('stock/del/<int:stock_id>/', views.stock_del, name='stock_del'),   # 削除
    path('shopping_list', views.shopping_list, name="shopping_list"),
    path('recipe/<int:num>', views.recipe, name="recipe"),
    path('customize', views.customize, name="customize"),

]