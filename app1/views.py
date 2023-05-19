from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("WELCOME TO GIT HUB PAGE")

<<<<<<< HEAD
def sales(request):
    return HttpResponse("Monthly Sales are 300")
=======
def app(request):
    return HttpResponse("welcome to app1 page")
>>>>>>> f39882f7589aab9b66f48933bd5839ea518dadb3
