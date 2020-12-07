from django.urls import path

from vkusnooo_auth.views import login_user, logout_user, register_user, user_profile

urlpatterns = (
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login view'),
    path('logout/', logout_user, name='logout view'),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
)
