from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import UserForm, BookForm
from .models import Book


def start(request):
    return render(request, 'first.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)


def hotel(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return render(request, 'hi.html', {'user': user})
    context = {
        "form": form,
    }
    return render(request, 'index.html', context)

