from django.shortcuts import render
from bbs.models import Post

def home_view(request):
    context = {}

    context['title'] = '一行掲示板'
    context['posts'] = Post.objects.all() 
    #ポストのテーブルからすべてのレコードを取得
    #レコードをDjangoのオブジェクトに変換する
    #<=>DBへのクエリを取得している<=>掲示板の利用者の投稿をすべて取得

    return render(request, 'bbs/home.html', context)
# Create your views here.
