from rest_framework import serializers
from .models import Film, Director, Review
from rest_framework.exceptions import ValidationError

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

class FilmValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=256)
    text = serializers.CharField(required=False) 
    rate_kp = serializers.FloatField(min_value=0, max_value=10)
    is_active = serializers.BooleanField()
    director_id = serializers.IntegerField(min_value=1)
    genres = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError("Director does not exist!")
        return director_id


