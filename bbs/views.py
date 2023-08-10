from django.shortcuts import render, redirect
from bbs.models import Post
from django.http import HttpResponse
from bbs.forms import PostForm

def home_view(request):
    #bbs/のテンプレートを出力するビュー
    
    #webページが要求してきたリクエストで分岐
    if request.method == 'GET':
        return home_view_get(request)
    elif request.method == 'POST':
        return home_view_post(request)
    else:
        return HttpResponse('invalid method', status=400)

def home_view_get(request, form=None):
    #bbs/のGET
    context = {}

    context['title'] = '一行掲示板'
    context['posts'] = Post.objects.all() 
    #ポストのテーブルからすべてのレコードを取得
    #レコードをDjangoのオブジェクトに変換する
    #<=>DBへのクエリを取得している<=>掲示板の利用者の投稿をすべて取得

    if form:
        context['form'] = form #form引数がNoneじゃなければその引数をコンテキストに
    else:
        context['form'] = PostForm() #フォームを保存？

    # renderにコンテキストを渡しテンプレートを描画
    return render(request, 'bbs/home.html', context)

def home_view_post(request):
    #bbs/のPOST

    form = PostForm(request.POST)

    #入力エラー時に getを呼び出してコンテキストに保存させている
    if not form.is_valid():
        return home_view_get(request, form=form)
    
    form.save()
    #ブラウザのリロードによるフォームからの2重送信を防ぐための処置
    return redirect('bbs_home')
    #↓これだとだめ
    #return home_view_get(request, form=form)

# Create your views here.
