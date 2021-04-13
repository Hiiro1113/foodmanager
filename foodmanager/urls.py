from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('schedule', views.schedule, name="schedule"),
    path('menu', views.menu, name="menu"),
    path('stock', views.stock, name="stock"),
    path('shopping_list', views.shopping_list, name="shopping_list"),
    path('recipe', views.recipe, name="recipe"),
    path('customize', views.customize, name="customize"),

]