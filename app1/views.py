from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("WELCOME TO GIT HUB PAGE")

def sales(request):
    return HttpResponse("Monthly Sales are 300")
def app(request):
    return HttpResponse("welcome to app1 page")
