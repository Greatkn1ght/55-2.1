from django.db import models
from datetime import datetime
# Create your models here.

class Director(models.Model):
    fio = models.CharField(max_length=255)
    birthday = models.DateField()

    def __str__(self):
        return self.fio
    
    def age(self):
        now = datetime.now()
        return now.year - self.birthday.year

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class Film(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    title = models.CharField(max_length=256)
    text = models.TextField(null=True, blank=True)
    rate_kp = models.FloatField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

STARS = ((i, '*' * i) for i in range(1,11))

class Review(models.Model):
    text = models.TextField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=2)

    def __str__(self):
        return self.stars