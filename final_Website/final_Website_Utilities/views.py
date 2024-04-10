from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

def team(request):
    return HttpResponse("Team")
