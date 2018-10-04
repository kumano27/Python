# -*- coding: utf-8 -*-

from django import forms

class HelloForm(forms.Form):
    # forms.CharField -> テキストを入力する一般的なフィールドクラス
    # forms.IntegerField -> 整数の値を入力するためのフィールドクラス
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')