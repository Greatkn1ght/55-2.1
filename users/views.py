from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterValidateSerializer, AuthValidationSerializer, ConfirmationCodeSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.

@api_view(['POST'])
def registration_api_view(request):
    # step 0: Validation
    serlializer = RegisterValidateSerializer(data=request.data)
    if not serlializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={'errors': serlializer.errors})
    
    # step 1: Create a user
    user = User.objects.create_user(
        username=serlializer.validated_data['username'],
        password=serlializer.validated_data['password'],
        is_active = False
        )
    # code (6-symbol)
    # step 2: Return response 
    return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id})

@api_view(['POST'])
def authorization_api_view(request):
    # step 0: Validation
    serializer = AuthValidationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # step 1: Authentication
    user = authenticate(
        username = serializer.validated_data['username'],
        password = serializer.validated_data['password']
    )

    # step 2: Return Token (get or create)
    if user is not None:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def confirm_user_view(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    cc = serializer.validated_data['confirmation']

    user.is_active = True
    user.save()

    cc.delete()

    return Response({'detail': "User activated"}, status=status.HTTP_200_OK)

    