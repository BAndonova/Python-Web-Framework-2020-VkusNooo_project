from django.urls import path

from vkusnooo_app.views import index, create_recipe, edit_recipe, details_recipe, delete_recipe

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('details/<int:pk>/', details_recipe, name='details recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
]