from django.urls import path
from .views import (
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView,
    ProductsWithReviewsAPIView,
)

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category_list_create'),
    path('categories/<int:id>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_detail'),

    path('products/', ProductListCreateAPIView.as_view(), name='product_list_create'),
    path('products/<int:id>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_detail'),
    path('products/reviews/', ProductsWithReviewsAPIView.as_view(), name='products_reviews'),

    path('reviews/', ReviewListCreateAPIView.as_view(), name='review_list_create'),
    path('reviews/<int:id>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review_detail'),
]