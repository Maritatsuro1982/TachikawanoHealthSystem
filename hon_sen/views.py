from django.shortcuts import render

def home(request):
    return render(request, 'hon_sen/home.html')

def about(request):
    return render(request, 'hon_sen/about.html')

def contact(request):
    return render(request, 'hon_sen/contact.html')

def register(request):
    return render(request, 'hon_sen/register.html')

