from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home(request):
    latest_articles = Article.objects.filter(is_published=True).order_by('-publication_date')[:3]
    context = {
        'latest_articles': latest_articles,
    }
    return render(request, 'blog/home.html', context)

def article_list(request):
    all_articles = Article.objects.filter(is_published=True)
    context = {
        'articles': all_articles,
    }
    return render(request, 'blog/article_list.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    context = {
        'article': article,
    }
    return render(request, 'blog/article_detail.html', context)

def category_list(request):
    all_categories = Category.objects.all()
    context = {
        'categories': all_categories,
    }
    return render(request, 'blog/category_list.html', context)