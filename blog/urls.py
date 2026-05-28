from django.urls import path
from .views import home
from django.shortcuts import render

urlpatterns = [
    path('', home, name='home'),

    path(
        'post/',
        lambda request: render(request, 'post_detail.html'),
        name='post_detail'
    ),
]