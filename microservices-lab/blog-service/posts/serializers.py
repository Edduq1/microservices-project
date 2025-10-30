from rest_framework import serializers
from .models import Post
from authors.serializers import AuthorSerializer # Importa el que acabas de crear
from categories.serializers import CategorySerializer # Importa el que acabas de crear

class PostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug','excerpt', 'author', 'category', 'published_at')

class PostDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug','excerpt', 'content', 'status',
                'author', 'category', 'created_at', 'published_at','views')
        read_only_fields = ('status', 'created_at', 'published_at')