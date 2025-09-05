from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Film
from django.forms import model_to_dict
from .serializers import FilmListSerializer, FilmDetailSerializer
# Create your views here.

@api_view(['GET'])
def film_details(reques, id):
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': 'Film not found!'})
    data = FilmDetailSerializer(film, many=False).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def film_list_api_view(request):
    films = Film.objects.all()
    data = FilmListSerializer(films, many=True).data
    return Response(
        data = data,
        status = status.HTTP_200_OK
    )
