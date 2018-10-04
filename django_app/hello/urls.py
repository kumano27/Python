# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # 複数ページの移動
    # path('next', views.next, name='next'),
    
    # フォームで送信
    # path('form', views.form, name='form'),
]