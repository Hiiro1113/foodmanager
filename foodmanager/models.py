from django.db import models
from django.contrib.auth.models import User
from album.models import Image

#スケジュールクラス
class Schedule(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    timing = models.CharField(max_length=20)
    menu_CD = models.ForeignKey('Menu', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.user_name

    class Meta:
        verbose_name = 'スケジュール'
        verbose_name_plural = 'スケジュール'

#買い物リストクラス
class Shopping_list(models.Model):
    shopping_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    food_CD = models.ForeignKey('Food', on_delete=models.CASCADE)
    date = models.DateField()
    timing = models.CharField(max_length=20)
    quantity = models.IntegerField()
    memo = models.CharField(max_length=100, null=True, blank=True)
    buy_date = models.DateTimeField(auto_now_add=True)
    buy_end = models.CharField(max_length=10)

    def __str__(self):
        return self.food_CD

    class Meta:
        verbose_name = '買い物リスト'
        verbose_name_plural = '買い物リスト'

#食材クラス
class Food(models.Model):
    food_CD = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    unit = models.CharField(max_length=5)
    expiration_date = models.IntegerField(default=1)

    def __str__(self):
        return self.food_name

    class Meta:
        verbose_name = '食材'
        verbose_name_plural = '食材'


#メニュークラス
class Menu(models.Model):
    menu_CD = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=30)
    popularity = models.IntegerField()
    menu_price = models.IntegerField()
    group = models.CharField(max_length=3)
    share = models.CharField(max_length=3)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu_name


    class Meta:
        verbose_name = 'メニュー'
        verbose_name_plural = 'メニュー'


#レシピクラス
class Recipe(models.Model):
    menu_CD = models.ForeignKey('Menu', on_delete=models.CASCADE)
    how_to_make = models.CharField(max_length=300)

    def __str__(self):
        return self.menu_CD


    class Meta:
        verbose_name = 'レシピ'
        verbose_name_plural = 'レシピ'



#使用食材クラス
class Use_food(models.Model):
    menu_CD = models.ForeignKey('Menu', on_delete=models.CASCADE)
    food_CD = models.ForeignKey('Food', on_delete=models.CASCADE)
    use_quantity = models.FloatField(default=1.0)

    def __str__(self):
        return self.food_CD.food_name


    class Meta:
        verbose_name = '使用食材'
        verbose_name_plural = '使用食材'



#在庫クラス
class Stock(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    food_CD = models.ForeignKey(Food, on_delete=models.CASCADE)
    stock_qntty = models.IntegerField()

    def __str__(self):
        return self.food_CD

    class Meta:
        verbose_name = '在庫'
        verbose_name_plural = '在庫'

#在庫履歴クラス
class Stock_history(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)
    history_id = models.AutoField(primary_key=True)
    food_CD = models.ForeignKey(Food, on_delete=models.CASCADE)
    in_out = models.CharField(max_length=10)
    buy_count = models.IntegerField()
    in_date = models.DateField(null=True, blank=True)
    use_date = models.DateField(null=True, blank=True)
    use_qntty = models.IntegerField()
    expiration = models.IntegerField()

    def __str__(self):
        return self.food_CD

    class Meta:
        verbose_name = '在庫履歴'
        verbose_name_plural = '在庫履歴'


