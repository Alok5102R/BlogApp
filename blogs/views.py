from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello")

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')