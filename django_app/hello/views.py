# 画面表示に関するもの
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from .forms import FindForm
from .forms import CheckForm
from django.db.models import Q # Q関数 OR条件に必要
from django.db.models import Count,Sum,Avg,Min,Max # 集計用の関数


def index(request):
    data = Friend.objects.all()
    # 指定項目のレコード数を返す
    re1 = Friend.objects.aggregate(Count('age'))
    # 指定項目の合計を計算
    re2 = Friend.objects.aggregate(Sum('age'))
    # 指定項目の平均を計算
    re3 = Friend.objects.aggregate(Avg('age'))
    # 指定項目の最小値を返す
    re4 = Friend.objects.aggregate(Min('age'))
    # 指定項目の最大値を返す
    re5 = Friend.objects.aggregate(Max('age'))

    msg = 'count:' + str(re1['age__count'])\
            + '<br>Sum:' + str(re2['age__sum'])\
            + '<br>Average:' + str(re3['age__avg'])\
            + '<br>Min:' + str(re4['age__min'])\
            + '<br>Max:' + str(re5['age__max'])
    params = {
                'title': 'Hello',
                'message':msg,
                'data': data,
            }
    return render(request, 'hello/index.html' , params)

# create model
def create(request):
    # POST送信されたか確認
    if (request.method == 'POST'):
        # Friend クラスのインスタンス作成(初期状態のインスタンス)
        obj = Friend()
        # FriendForm インスタンス作成
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
                'title': 'Helo',
                'form': FriendForm(),
            }
    return render(request, 'hello/create.html',params)

def edit(request, num):
    # インスタンスの取得 -> 引数id
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        # instance 引数に get で取得したインスタンスを指定
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
                'title': 'Hello',
                'id':num,
                'form': FriendForm(instance=obj),
            }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
                'title': 'Hello',
                'id': num,
                'obj': friend,
            }
    return render(request, 'hello/delete.html', params)

def find(request):
    if(request.method == 'POST'):
        # POST送信されている事を確認し、変数sqlにアクセスするSQLクエリ文を用意
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from hello_friend'
        
        # フォームから何かテキストが送信されてきた場合
        if(msg != ''):
            sql += ' where ' + msg
        
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
            'title': 'Hello',
            'message': msg,
            'form': form,
            'data':data,
            }

    return render(request, 'hello/find.html', params)

def check(request):
    params = {
                'title': 'Hello',
                'message': 'check validation.',
                'form': FriendForm(),
            }
    if(request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if(form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/check.html', params)