from django.shortcuts import render
# 画面表示に関するもの
# Create your views here.

from django.http import HttpResponse

# Formクラスを作成する
from .forms import HelloForm

def index(request):
    # HTTPレスポンスで Django ページの表示確認
    # return HttpResponse("Hello Django!!")
    
    # クエリパラメータの表示
    # msg = request.GET['msg']
    # return HttpResponse('you typed: "' + msg + '".')
    
    # テンプレートを使ってみる
    # return render(request, 'hello/index.html')

    """
    # テンプレートに値を渡してみる
    params = {
                'title':'Hello/Index',
                # 'msg':'これは、サンプルで作ったページです。',
                # フォームで送信
                'msg':'お名前は？',
                # 複数ページの移動
                'goto':'next',
            }
    return render(request, 'hello/index.html', params)
    """
    
    # Formクラスを作成する
    params = {
                'title':'Hello',
                'message':'your data:',
                'form':HelloForm()
            }
    if(request.method == 'POST'):
        params['message'] = '名前:' + request.POST['name'] + \
        '<br>メール:' + request.POST['mail'] + \
        '<br>年齢:' + request.POST['age']
        params['form'] = HelloForm(request.POST)
        
    return render(request, 'hello/index.html', params)

"""
# 複数ページの移動
def next(request):
    params = {
                'title':'Hello/Next',
                'msg':'これは、もう1つのページです。',
                'goto':'index',
            }
    return render(request, 'hello/index.html', params)
"""

def form(request):
    msg = request.POST['msg']
    params = {
                'title':'Hello/Form',
                'msg':'こんにちは、　' + msg + '　さん。',
            }
    return render(request, 'hello/index.html', params)