from django.db import models
from embed_video.fields import EmbedVideoField

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
    type = models.CharField(max_length=20, choices=MEAL_TYPES, default='')
    title = models.CharField(max_length=30)
    # image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='pictures')
    video = models.ImageField(upload_to='videos')
    time = models.IntegerField()
    # likes = models.ManyToManyField(to=Recipe)

    def __str__(self):
        return f'{self.id}; {self.title}; {self.time}'


class Like(models.Model):
    pets = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)


class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()