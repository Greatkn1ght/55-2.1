from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError

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
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = 'name products_count'.split()

    def get_products_count(self, obj):
        return obj.product_set.count()
        
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title description price category'.split()

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text product stars'.split()

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length = 1, max_length=200)

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=256)
    description = serializers.CharField(required=False)
    price = serializers.FloatField(min_value=1)
    category = serializers.IntegerField(min_value=1)

    def validate_category_id(self, category):
        try:
            Category.objects.get(id=category)
        except Category.DoesNotExist:
            raise ValidationError("Category does not exist")
        return category
    
class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=False)
    product = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_product_id(self, product):
        try:
            Product.objects.get(id=product)
        except Product.DoesNotExist:
            raise ValidationError("Product does not exist")
        return product

