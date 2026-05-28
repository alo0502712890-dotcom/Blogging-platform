from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import RegisterForm

def home(request):

    posts = [
        {
            'title': 'First Blog Post',
            'content': 'This is our first Django blog platform article.',
            'author': 'Sofia'
        },

        {
            'title': 'Bootstrap Integration',
            'content': 'We connected Blogy template to Django.',
            'author': 'Alona'
        },

        {
            'title': 'Python Django',
            'content': 'Our project is finally working.',
            'author': 'Team'
        }
    ]

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

            login(request, user)

            return redirect("home")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})