from django import forms
from django.contrib.auth.models import User
from .models import Book


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['From', 'To', 'Type', 'requirements', 'adults', 'children', 'name', 'Email', 'phone']
