from django.shortcuts import render

def home(request):
    return render(request, "mainPage.html")

def product(request):
    return
