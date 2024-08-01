from django.shortcuts import render, redirect
from .models import Article 
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()
    
    context = {
        'article' : article,
        'form' : form,
    }

    return render(request, 'detail.html', context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)    # 방금 사용자가 입력한 데이터도 담아서
        
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
    
    else:
        form = ArticleForm()

    context = {
        'form' : form,
    }

    return render(request, 'form.html', context)


def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)    # form 임시 저장, commit은 하지마!

            # 1. 객체를 저장하는 방법
            article = Article.objects.get(id=article_id)
            comment.article = article
            comment.save()

            return redirect('articles:detail', id=article_id)

    else:
        return redirect('article:index')











