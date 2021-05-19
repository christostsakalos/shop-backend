from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category, Parentcategory
from .serializers import ProductSerializer, CategorySerializer, ParentcategorySerializer
# Create your views here.

# User views
class LatestProductsList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, parentcategory_slug, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request,parentcategory_slug, category_slug, product_slug, format=None):
        product = self.get_object(parentcategory_slug, category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ParentCategoriesList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        
        parentcategories = Parentcategory.objects.all()
        serializer = ParentcategorySerializer(parentcategories, many=True)
        return Response(serializer.data)

class ParentcategoryDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, parentcategory_slug):
        try:
            return Parentcategory.objects.get(slug=parentcategory_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, parentcategory_slug, format=None):
        parentcategory = self.get_object(parentcategory_slug)
        serializer = ParentcategorySerializer(parentcategory)
        return Response(serializer.data)

class CategoryDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, parentcategory_slug, category_slug):
        try:
            return Category.objects.filter(parent__slug=parentcategory_slug).get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request,parentcategory_slug, category_slug, format=None):
        category = self.get_object(parentcategory_slug, category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

# Admin views

class ParentcategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ParentcategorySerializer
    queryset = Parentcategory.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)