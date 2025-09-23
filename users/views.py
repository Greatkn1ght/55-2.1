from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def registration_api_view(request):
    # step 0: Validation
    # step 1: Create a user
    # step 2: Return response 
    return Response()