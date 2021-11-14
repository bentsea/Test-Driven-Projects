from django.shortcuts import render, HttpResponse

def home_page(request):
    return HttpResponse("<html><body><title>Untitled Cooking Project</title><h1>Hello World!</h1></body></html>")
