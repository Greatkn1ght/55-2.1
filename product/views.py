from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from django.forms import model_to_dict
from .serializers import CategoryListSerializer, ProductListSerializer, ReviewListSerializer
from .serializers import CategoryDetailSerializer, ProductDetailSerializer, ReviewDetailSerializer
from .serializers import CategoryValidateSerializer, ProductValidateSerializer, ReviewValidateSerializer
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.generics import(
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
# Create your views here.

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryValidateSerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryValidateSerializer
    lookup_field = 'id'

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer
    lookup_field = 'id'

class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewValidateSerializer


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewValidateSerializer
    lookup_field = 'id'


class ProductsWithReviewsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = []

        for product in products:
            reviews = product.reviews.all()
            avg_rating = reviews.aggregate(Avg('stars'))['stars__avg']
            data.append({
                'id': product.id,
                'title': product.title,
                'description': product.description,
                'price': product.price,
                'category': product.category.name,
                'rating': round(avg_rating, 2) if avg_rating else None,
                'reviews': ReviewValidateSerializer(reviews, many=True).data
            })

        return Response(data)