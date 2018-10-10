# -*- coding: utf-8 -*-

from django import forms
from.models import Friend

class HelloForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label='Gender',required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')
    
class FriendForm(forms.ModelForm):
    # メタクラス
    class Meta:
        # モデルクラス
        model = Friend
        # フィールド
        fields = ['name','mail','gender','age','birthday']