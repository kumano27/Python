from django.shortcuts import render
# 画面表示に関するもの
# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView

# Formクラスを作成する
from .forms import HelloForm

class HelloView(TemplateView):
    
    """
    # クラスに用意されている初期メソッド
    # 「self.params」 に値を用意
    """
    def __init__(self):
        self.params = {
                    'title':'Hello',
                    'form':HelloForm(),
                    'result':None
                }
    
    """
    # GETアクセス時に実行される処理
    # 「self.params」 をそのままrender
    """
    def get(self, request):
        return render(request, 'hello/index.html', self.params)
    
    
    """
    # POST送信時の処理
    # request.POST から値を取り出してメッセージを作成し、
    # self.parmas['message'] に設定
    
    # request.POST を引数に HelloForm インスタンス作成後
    # self.params['form'] に設定
    """
    def post(self, request):
        if('check' in request.POST):
            # チェックがONの時
            self.params['result'] = 'Checked!!'
        else:
            # チェックがOFFの時
            self.params['result'] = 'not checked...'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
    