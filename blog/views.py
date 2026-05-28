from django.shortcuts import render


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