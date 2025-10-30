from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets, mixins
from rest_framework import filters
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer

@method_decorator(cache_page(60), name="retrieve")   # detalle cacheado 60s
class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.filter(status="published").select_related("author", "category")
    filterset_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]
    def get_serializer_class(self):
        return PostDetailSerializer if self.action == "retrieve" else PostListSerializer
