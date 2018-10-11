# 画面表示に関するもの
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from .forms import FindForm
from django .db.models import Q # Q関数 OR条件に必要

def index(request):
    # reverse -> 降順
    data = Friend.objects.all().order_by('age').reverse()
    params = {
                'title': 'Hello',
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
        msg = 'search result:'
        form = FindForm(request.POST)
        # テキストを分割してリストへ
        str = request.POST['find']
        list = str.split()
        # 送られた値を元にallで得た中から指定範囲のレコードだけを取り出す
        data = Friend.objects.all()[int(list[0]):int(list[1])]
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
                'title':'Hello',
                'message':msg,
                'form':form,
                'data':data,
            }
    return render(request, 'hello/find.html', params)
        