from django.urls import path
from . import views


urlpatterns = [
    path('', views.schedule, name="schedule"),
    path('menu', views.menu, name="menu"),
    path('stock', views.stock, name="stock"),
    path('shopping_list', views.shopping_list, name="shopping_list"),
    path('recipe/<int:num>', views.recipe, name="recipe"),
    path('customize', views.customize, name="customize"),

]