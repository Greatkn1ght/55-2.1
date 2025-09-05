from rest_framework import serializers
from .models import Category, Product, Review

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()
        
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title description price category'.split()

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text'.split()