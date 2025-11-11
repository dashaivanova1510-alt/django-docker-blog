from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.article_list, name='article-list'),
    path('article/<int:pk>/', views.article_detail, name='article-detail'),
    path('categories/', views.category_list, name='category-list'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
]