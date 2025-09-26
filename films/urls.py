from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list_create_api_view),
    path('<int:id>/', views.film_details),
    path('genres/', views.GenreListAPIView.as_view()),
    path('genres/<int:id>/', views.GenreDetailAPIView.as_view())
]