from rest_framework import serializers
from .models import Posts
from authors.serializers import AuthorSerializer # Importa el que acabas de crear
from categories.serializers import CategorySerializer # Importa el que acabas de crear

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'author', 'category', 'published_at')

class PostDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'content', 'status',
                'author', 'category', 'created_at', 'published_at')
        read_only_fields = ('status', 'created_at', 'published_at')