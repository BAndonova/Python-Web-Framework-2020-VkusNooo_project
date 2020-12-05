from django.urls import path

from vkusnooo_auth.views import login_user, logout_user, register_user

urlpatterns = (
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login view'),
    path('logout/', logout_user, name='logout view'),
)
