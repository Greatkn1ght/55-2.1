from django.db import models
from django.db.models import Avg

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

STARS = ((i, '*' * i) for i in range(1,6))
class Review(models.Model):
    text = models.TextField(null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    stars = models.IntegerField(choices=STARS, default=2)

    def __str__(self):
        avg = Review.objects.aggregate(Avg('stars'))['stars__avg']
        return f"{self.text} Average rating: {avg:.1f}"
