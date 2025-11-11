from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    icon = models.CharField(max_length=50, verbose_name="Іконка Font Awesome")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name="Тег")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст статті")
    image = models.URLField(verbose_name="Посилання на зображення")
    publication_date = models.DateField(auto_now_add=True, verbose_name="Дата публікації")
    is_published = models.BooleanField(default=False, verbose_name="Опубліковано")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
        ordering = ['-publication_date']

class Comment(models.Model):
    text = models.TextField(verbose_name="Текст коментаря")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Автор")
    author_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ім'я анонімного автора")
    publication_date = models.DateField(auto_now_add=True, verbose_name="Дата публікації")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="Стаття")

    def get_author_name(self):
        """Повертає ім'я автора: або з профілю, або з поля author_name."""
        if self.author:
            return self.author.username
        return self.author_name or "Анонім"

    def __str__(self):
        return f"Коментар від {self.author} до статті '{self.article.title}'"

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ['-publication_date']