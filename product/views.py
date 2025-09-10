from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from django.forms import model_to_dict
from .serializers import CategoryListSerializer, ProductListSerializer, ReviewListSerializer
from .serializers import CategoryDetailSerializer, ProductDetailSerializer, ReviewDetailSerializer
from django.db.models import Avg
# Create your views here.

@api_view(['GET', 'POST'])
def shop_category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategoryListSerializer(categories, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(
            name = name
        )
        category.save()
        return Response(status=status.HTTP_201_CREATED,
                        data = CategoryDetailSerializer(category).data)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'Category not found!'})
    if request.method == 'GET':
        data =  CategoryDetailSerializer(category, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response(status=status.HTTP_201_CREATED,
                        data = CategoryDetailSerializer(category).data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def shop_product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductListSerializer(products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category = request.data.get('category')

        product = Product.objects.create(
            title = title,
            description = description,
            price = price, 
            category = category
        )
        product.save()

        return Response(status=status.HTTP_201_CREATED,
                        data = ProductDetailSerializer(product).data)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'Product not found!'})
    if request.method == 'GET':
        data =  ProductDetailSerializer(product, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category = request.data.get('category')
        product.save()

        return Response(status=status.HTTP_201_CREATED,
                        data = ProductDetailSerializer(product).data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def review(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewListSerializer(reviews, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        product = request.data.get('product')
        stars = request.data.get('stars')

        review = Review.objects.create(
            text = text,
            product = product,
            stars = stars
        )
        review.save()
        
        return Response(status=status.HTTP_201_CREATED,
                        data = ReviewDetailSerializer(review).data)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, id):
    try:
        review_details = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'Review not found!'})
    if request.method == 'GET':
        data =  ReviewDetailSerializer(review_details, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        review_details.text = request.data.get('text')
        review_details.product = request.data.get('product')
        review_details.stars = request.data.get('stars')
        review_details.save()
        return Response(status=status.HTTP_201_CREATED,
                        data = ReviewDetailSerializer(review_details).data)
    elif request.method == 'DELETE':
        review_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def product_rating(request):
    rating = Review.objects.aggregate(Avg('stars'))['stars__avg']
    return Response({'average_rating': round(rating, 1) if rating else None})