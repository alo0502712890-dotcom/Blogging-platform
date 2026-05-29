from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CommentForm
from .forms import RegisterForm, PostForm

from .models import Profile, Post
from .models import Category



def home(request):
    posts = Post.objects.filter(
        status="published"
    )

    query = request.GET.get("q")

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    return render(
        request,
        'home.html',
        {'posts': posts}
    )

def about_view(request):
    return render(request, "about.html")


def contact_view(request):
    return render(request, "contact.html")


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
    if request.method == "POST" and request.user.is_authenticated:

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)

            comment.post = post
            comment.author = request.user

            comment.save()

            return redirect(
                "post_detail",
                post_id=post.id
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

def category_list(request):

    categories = Category.objects.all()

    return render(
        request,
        'category.html',
        {'categories': categories}
    )

@login_required
def profile_view(request):

    posts = Post.objects.filter(author=request.user)

    return render(
        request,
        'profile.html',
        {
            'posts': posts
        }
    )

@login_required
def update_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )

    if request.method == "POST":

        form = PostForm(
            request.POST,
            instance=post
        )

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:

        form = PostForm(instance=post)

    return render(
        request,
        "update_post.html",
        {"form": form}
    )

@login_required
def delete_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )

    if request.method == "POST":

        post.delete()

        return redirect("profile")

    return render(
        request,
        "delete_post.html",
        {"post": post}
    )

def category_posts(request, category_id):

    category = get_object_or_404(
        Category,
        id=category_id
    )

    posts = Post.objects.filter(
        category=category,
        status="published"
    )

    return render(
        request,
        "home.html",
        {
            "posts": posts
        }
    )