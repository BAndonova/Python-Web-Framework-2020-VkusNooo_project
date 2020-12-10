from django.contrib import admin

from vkusnooo_auth.models import UserProfile

admin.site.register(UserProfile)


# class UserInLine(admin.TabularInline):
#     model = UserProfile
#
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'profile_image', 'username', 'date_of_birth', 'creation_date')
#     list_filter = ('user', 'profile_image', 'username', 'date_of_birth', 'creation_date')
#     # inlines = (
#     #     UserInLine,
#     # )
