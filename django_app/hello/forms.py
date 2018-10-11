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
    # 空の入力を許可するか指定
    empty = forms.CharField(label='Empty', empty_value=True)
    
    # 入力するテキストの最小文字数を指定
    # 以下の例だと10文字以上を入力する必要がある
    min = forms.CharField(label='Min', min_length=10)
    # 入力するテキストの最大文字数を指定
    # 以下の例だと10文字以下の入力のみ受け付ける
    max = forms.CharField(label='Max', max_length=10)