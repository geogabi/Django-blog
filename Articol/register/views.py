from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return redirect('/register')
    else:
        form = RegisterForm()
    return render(response, 'register/register.html',{'form':form})


def login_usr(response):
    if response.method == 'POST':
        username = response.POST['username']
        password = response.POST['password']
        user = authenticate(response,username=username, password=password)
        if user is not None:
            login(response,user)
            return redirect('/home')
        else:
            return redirect('/login')
    return render(response, 'register/login.html')

def log_out(response):
    logout(response)
    return redirect('/home')
