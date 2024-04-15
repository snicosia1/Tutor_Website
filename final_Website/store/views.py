from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})


def tutor(request):
    return render(request, 'tutor.html', {})


def classes(request):
    return render(request,'class.html',{})


def faq(request):
    return render(request,'faq.html',{})


def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

