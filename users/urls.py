from django.urls import path
from .views import RegistrationAPIView, AuthorizationAPIView, ConfirmationAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='user-registration'),
    path('authorization/', AuthorizationAPIView.as_view(), name='user-authorization'),
    path('confirmation/', ConfirmationAPIView.as_view(), name='user-confirmation'),
]