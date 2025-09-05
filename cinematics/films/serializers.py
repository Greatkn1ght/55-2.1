from rest_framework import serializers
from .models import Film, Director, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()
        
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id fio age'.split()

class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        
class FilmListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    genres = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Film
        # fields = ['id', 'title', 'text', 'rate_kp', 'created']
        fields = 'id director genres reviews title text rate_kp created'.split(' ')
        # depth = 1
        # fields = '__all__'
        # exlude = 'text,rate_kp'.split(',')

    def get_genres(self, film):
        return [i.name for i in film.genres.all()]
