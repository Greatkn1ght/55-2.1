from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from django.forms import model_to_dict
from .serializers import CategoryListSerializer, ProductListSerializer, ReviewListSerializer
from .serializers import CategoryDetailSerializer, ProductDetailSerializer, ReviewDetailSerializer
# Create your views here.

@api_view(['GET'])
def shop_category(request):
    categories = Category.objects.all()
    data = CategoryListSerializer(categories, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'Category not found!'})
    data =  CategoryDetailSerializer(category, many=False).data
    return Response(data=data)

@api_view(['GET'])
def shop_product(request):
    products = Product.objects.all()
    data = ProductListSerializer(products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'Product not found!'})
    data =  ProductDetailSerializer(product, many=False).data
    return Response(data=data)

@api_view(['GET'])
def review(request):
    reviews = Review.objects.all()
    data = ReviewListSerializer(reviews, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_detail(request, id):
    try:
        review_details = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'Review not found!'})
    data =  ReviewDetailSerializer(review_details, many=False).data
    return Response(data=data)