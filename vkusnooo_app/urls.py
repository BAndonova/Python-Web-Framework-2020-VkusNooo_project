from django.urls import path

from vkusnooo_app.views import index, create_recipe, edit_recipe, details_recipe, delete_recipe, desserts, meat_meals, \
    meatless_meals, other, pasta_dough, vegan, healthy, all_recipes, like_recipe

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('details/<int:pk>/', details_recipe, name='details recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('recipes/', all_recipes, name='all recipes'),
    path('desserts/', desserts, name='desserts'),
    path('meat/', meat_meals, name='meat meals'),
    path('meatless/', meatless_meals, name='meatless meals'),
    path('other/', other, name='other'),
    path('pasta/', pasta_dough, name='pasta and dough'),
    path('vegan/', vegan, name='vegan'),
    path('healthy/', healthy, name='healthy and dietetic'),
    path('like/<int:pk>/', like_recipe, name='like recipe'),
]
