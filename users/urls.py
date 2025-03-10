from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('password', views.reset_password, name='password'),
    path('profile', views.view_profile, name='profile'),
]