from django import forms
from django.contrib.auth.models import User
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture', 'title']


class StockForm(forms.ModelForm):
    """在庫のフォーム"""
    class Meta:
        model = Stock
        fields = '__all__'