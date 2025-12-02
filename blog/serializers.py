from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) 

    class Meta:
        model = Article
        fields = '__all__'