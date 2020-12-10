from django.contrib import admin

from vkusnooo_auth.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'creation_date')
    list_filter = ('creation_date','date_of_birth',)


admin.site.register(UserProfile, UserProfileAdmin)