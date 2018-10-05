# -*- coding: utf-8 -*-

from django import forms

class HelloForm(forms.Form):
    data = [
                ('one', 'radio 1'),
                ('two', 'radio 2'),
                ('three', 'radio 3')
            ]
    # RadioSelect -> ウィジェット(Webページに表示されるHTMLタグをかんるするクラス)
    # 今回の例だと widget 引数に RadioSelect を設定
    choice = forms.ChoiceField(label='radio', \
                               choices=data, widget=forms.RadioSelect())