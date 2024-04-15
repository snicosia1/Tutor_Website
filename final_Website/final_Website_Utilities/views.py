from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

def team(request):
    return HttpResponse("Team")
    
def about(request):
    return HttpResponse("About")

def faq(request):
    return HttpResponse("Faq")

def classes(request):
    return HttpResponse("Classes")

def contact(request):
    return HttpResponse("Contact")
