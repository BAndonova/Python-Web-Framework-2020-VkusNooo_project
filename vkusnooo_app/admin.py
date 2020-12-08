from django.contrib import admin

# Register your models here.
from vkusnooo_app.models import Recipe, Like

admin.site.register(Recipe)
admin.site.register(Like)

class LikeInline(admin.TabularInline):
    model = Like


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'title', 'time')
    list_filter = ('type', 'age')
    inlines = (
        LikeInline,
    )
