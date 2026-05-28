from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, PostForm
from .models import Profile, Post


def home(request):
    posts = Post.objects.filter(status="published")
    return render(
        request,
        'home.html',
        {'posts': posts}
    )


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile.objects.create(
                user=user,
                role=Profile.ROLE_READER
            )

            login(request, user)

            return redirect("home")

    else:
        form = RegisterForm()

    return render(
        request,
        "register.html",
        {"form": form}
    )


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id
    )
    return render(
        request,
        'post_detail.html',
        {'post': post}
    )

@login_required
def create_post(request):

    if request.user.profile.role not in ["author", "admin"]:
        return redirect("home")

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect("home")

    else:
        form = PostForm()

    return render(
        request,
        'create_post.html',
        {'form': form}
    )