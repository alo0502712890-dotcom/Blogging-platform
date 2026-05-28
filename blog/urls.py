from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home, register_view


urlpatterns = [
    path('', home, name='home'),

    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
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
path(
    'profile/',
    lambda request: render(request, 'profile.html'),
    name='profile'
),
path(
    'category/',
    lambda request: render(request, 'category.html'),
    name='category'
),
]