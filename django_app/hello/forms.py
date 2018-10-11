# -*- coding: utf-8 -*-

from django import forms
from.models import Friend
from django import forms

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
    str = forms.CharField(label='String')
    
    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if(str.lower().startswith('no')):
            # no で始まるテキストを入力すると下記メッセージ表示
            raise forms.ValidationError('You input "NO"!')