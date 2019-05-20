from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Movie_Review(models.Model):
    User= models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title= models.TextField(default=False)
    year= models.IntegerField(default=False)
    poster=models.URLField(default=False)
    movietype = models.TextField(default=False)
    reviewrating = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    imdb = models.CharField(max_length = 200,default=False)
    reviewcategory = models.CharField(default=False,max_length = 100)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')