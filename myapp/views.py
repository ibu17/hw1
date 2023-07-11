from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout,get_user
from django.contrib.auth.forms import UserCreationForm
from .models import Person
from .forms import PersonForm
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        persons = Person.objects.filter(user=get_user(request))
        return render(request, 'home.html', {'persons': persons})
    else:
        return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('/')
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def add_birthday(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            birthday = request.POST['birthday']
            user=get_user(request)
            person=Person(user=user,name=name, birthday=birthday)
            person.save()
            persons=Person.objects.filter(user=user)
            return render(request, 'home.html', {'persons': persons})
    else:
        form = PersonForm()
    return render(request, 'birthday.html')

def birthday_list(request):
    persons = Person.objects.filter(user=get_user(request))
    return render(request, 'home.html', {'persons': persons})