from django.contrib import admin  # <-- Додайте цей імпорт
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # <-- Додайте цей рядок
    path('', include('blog.urls')),
]