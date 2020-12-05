from django.contrib import admin

# Register your models here.
from vkusnooo_app.models import Recipe, Like

admin.site.register(Recipe)
admin.site.register(Like)

