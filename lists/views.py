from django.shortcuts import render, HttpResponse

def home_page(request):
    return HttpResponse("<html><body><title>Untitled Cooking Project</title><h1>Untitled Cooking Project</h1></body></html>")
