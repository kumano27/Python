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
    # 日付を表す整数(1～31 の間の数)が入力可能
    date = forms.DateField(label='Date', input_formats=['%d'])
    # hh:mm形式でなければエラー
    time = forms.TimeField(label='Time')
    #　mm/dd/yyyy_hh:mm 形式でなければエラー
    datetime = forms.DateTimeField(label='DateTime')