from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Article, Category, Comment
from .forms import CommentForm

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
    
    if request.method == 'POST':
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
            return redirect('article-detail', pk=article.pk)
    else:
        form = CommentForm(user=request.user)

    is_moderator = False
    if request.user.is_authenticated:
        is_moderator = request.user.groups.filter(name='moderator').exists()

    context = {
        'article': article,
        'form': form,
        'is_moderator': is_moderator, 
    }
    return render(request, 'blog/article_detail.html', context)

def category_list(request):
    all_categories = Category.objects.all()
    context = {
        'categories': all_categories,
    }
    return render(request, 'blog/category_list.html', context)

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.user != comment.author:
        raise PermissionDenied

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('article-detail', pk=comment.article.pk)
    else:
        form = CommentForm(instance=comment, user=request.user)
    
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    is_author = request.user == comment.author
    is_moderator = request.user.groups.filter(name='moderator').exists()

    if not (is_author or is_moderator):
        raise PermissionDenied

    if request.method == 'POST':
        article_pk = comment.article.pk
        comment.delete()
        return redirect('article-detail', pk=article_pk)
    
    return render(request, 'blog/delete_comment.html', {'comment': comment})