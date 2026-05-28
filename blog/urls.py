from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home, register_view, post_detail, create_post, profile_view, category_list, about_view, contact_view, \
    delete_post, update_post

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
        profile_view,
        name='profile'
    ),
    path(
        "post/<int:post_id>/edit/",
        update_post,
        name="update_post"
    ),

    path(
        "post/<int:post_id>/delete/",
        delete_post,
        name="delete_post"
    ),
    path(
        'category/',
        category_list,
        name='category'
    ),
    path(
        "about/",
        about_view,
        name="about"
    ),

    path(
        "contact/",
        contact_view,
        name="contact"
    ),

]