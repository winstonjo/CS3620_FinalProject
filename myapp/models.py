from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="Enter a brief description")
    ingredients = models.TextField(blank=True, help_text="Enter ingredients")
    instructions = models.TextField(blank=True, help_text='Enter instructions')
    prep_time = models.IntegerField(help_text="Preparation time in minutes")
    cook_time = models.IntegerField(help_text="Cooking time in minutes")
    cuisine = models.ForeignKey('Cuisine', on_delete=models.SET_NULL, null=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Cuisine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.author





