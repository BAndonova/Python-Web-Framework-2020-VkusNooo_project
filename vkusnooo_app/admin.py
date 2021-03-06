from django.contrib import admin

# Register your models here.
from vkusnooo_app.models import Recipe, Like


# class LikeInline(admin.TabularInline):
#     model = Like


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'title', 'time', 'created_by',)
    list_filter = ('type', 'time', 'created_by')
    # inlines = (
    #     LikeInline,
    # )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Like)
