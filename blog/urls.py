from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home, register_view, post_detail, create_post

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
        'post/<int:post_id>/',
        post_detail,
        name='post_detail'
    ),
    path(
        'create/',
        create_post,
        name='create_post'
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