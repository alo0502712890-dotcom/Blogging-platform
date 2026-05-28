from django.contrib.auth import login
from django.shortcuts import render, redirect

from .models import Post
from .forms import RegisterForm, PostForm


def home(request):

    posts = Post.objects.all()

    return render(
        request,
        'home.html',
        {'posts': posts}
    )


def create_post(request):

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            form.save_m2m()

            return redirect('/')

    else:

        form = PostForm()

    return render(
        request,
        'create_post.html',
        {'form': form}
    )


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("home")

    else:

        form = RegisterForm()

    return render(
        request,
        "register.html",
        {"form": form}
    )