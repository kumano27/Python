# -*- coding: utf-8 -*-

from django import forms
from.models import Friend

class HelloForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    # required -> 「必須項目」として設定する為のバリデーション機能
    # required=False　-> 必須扱いとしない
    gender = forms.BooleanField(label='Gender',required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth',required=False)
    
class FriendForm(forms.ModelForm):
    # メタクラス
    class Meta:
        # モデルクラス
        model = Friend
        # フィールド
        fields = ['name','mail','gender','age','birthday']
        
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)
    
class CheckForm(forms.Form):
    # 必須項目とするか否か
    required = forms.IntegerField(label='Required')
    # 入力する数値の最小値を指定
    # 以下の例だと100以上を入力する必要がある
    min = forms.IntegerField(label='Min', min_value=100)
    # 入力する数値の最大値を指定
    # 以下の例だと100以下の入力のみ受け付ける
    max = forms.IntegerField(label='Max', max_value=100)