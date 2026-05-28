from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Comment


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Ім'я користувача",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введіть ім'я"
        })
    )

    email = forms.EmailField(
        label="Електронна пошта",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Введіть email"
        })
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Введіть пароль"
        })
    )

    password2 = forms.CharField(
        label="Підтвердження пароля",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Повторіть пароль"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            "title",
            "slug",
            "content",
            "category",
            "tags",
            "status"
        ]

        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter title"
            }),

            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "enter-title-slug"
            }),

            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 8,
                "placeholder": "Write your article..."
            }),

            "category": forms.Select(attrs={
                "class": "form-select"
            }),

            "tags": forms.SelectMultiple(attrs={
                "class": "form-select"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),
        }

        labels = {
            "title": "Title",
            "slug": "Slug",
            "content": "Content",
            "category": "Category",
            "tags": "Tags",
            "status": "Status",
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]