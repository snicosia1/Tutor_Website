from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from .models import Tutor, Product, Customer, Order 


def home(request):
    return render(request, 'index.html', {})


def tutor(request):
    tutors = Tutor.objects.all()
    return render(request, 'tutor.html', {'tutors': tutors})


def classes(request):
    all_Products = Product.objects.all()
    return render(request,'class.html', {'all_Products': all_Products})

def add_class(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            product = request.POST.get()
            user = request.user
            currCustomer = Customer.objects.get(user=user)
            currCustomer.products.add(product)
    return render(request, 'class.html', {})


def faq(request):
    return render(request,'faq.html',{})


def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, ("There was an error, try again!"))
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #login in user
            user = authenticate(username=username, password=password)
            login(request, user)
            customer_instance = Customer.objects.create(user=user)
            messages.success(request, 'Account created successfully')
            return redirect('home')
        else:
            messages.success(request, 'There was a problem registering')
            return redirect('register')

    else:
        return render(request,'register.html',{'form':form})