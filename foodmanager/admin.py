from django.contrib import admin
from .models import Schedule,Shopping_list,Stock,Stock_history,Food,Menu,Use_food,Recipe
# Register your models here.

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'date', 'timing', 'menu_CD')

class Shopping_listAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'food_CD', 'date', 'timing', 'quantity', 'buy_date', 'buy_end')

class StockAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'food_CD', 'stock_qntty',)

class Stock_historyAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'food_CD', 'in_out', 'buy_count', 'in_date', 'use_date', 'use_qntty', 'expiration')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'price', 'unit', 'expiration_date')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'popularity', 'menu_price')

class Use_foodAdmin(admin.ModelAdmin):
    list_display = ('menu_CD', 'food_CD', 'use_quantity', )



admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Shopping_list, Shopping_listAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Stock_history, Stock_historyAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Use_food, Use_foodAdmin)
admin.site.register(Recipe)
