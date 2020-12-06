from django.contrib.auth.models import User
from django.db import models
from embed_video.fields import EmbedVideoField

from vkusnooo_auth.models import UserProfile


class Recipe(models.Model):
    Meat_Meals = 'Meat Meals'
    Pasta_and_Dough = 'Pasta and Dough'
    Meatless_Meals = 'Meatless Meals'
    Healthy_and_Dietetic = 'Healthy and Dietetic'
    Vegan = 'Vegan'
    Desserts = 'Desserts'
    Other = 'Other'
    MEAL_TYPES = (
        (Meat_Meals, 'Meat Meals'),
        (Pasta_and_Dough, 'Pasta and Dough'),
        (Meatless_Meals, 'Meatless Meals'),
        (Healthy_and_Dietetic, 'Healthy and Dietetic'),
        (Vegan, 'Vegan'),
        (Desserts, 'Desserts'),
        (Other, 'Other'),
    )
    type = models.CharField(max_length=100, choices=MEAL_TYPES, default='', blank=False)
    title = models.CharField(max_length=100)
    # image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(max_length=10000)
    photo = models.ImageField(upload_to='pictures', blank=True)
    video = models.ImageField(upload_to='videos', blank=True)
    time = models.IntegerField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.id}; {self.title}; {self.time}'


class Like(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
