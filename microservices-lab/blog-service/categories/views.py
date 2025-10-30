from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

@method_decorator(cache_page(60*2, key_prefix="categories"), name='get') # Cachear por 2 minutos
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True) # Solo activas
    serializer_class = CategorySerializer