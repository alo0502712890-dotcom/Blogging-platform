from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import render

from .views import (
    home,
    register_view,
    create_post
)

urlpatterns = [

    path('', home, name='home'),

    path(
        'post/',
        lambda request: render(request, 'post_detail.html'),
        name='post_detail'
    ),

    path(
        'create/',
        create_post,
        name='create_post'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'register/',
        register_view,
        name='register'
    ),
]