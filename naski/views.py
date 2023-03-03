from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'naski/index.html')

def dashboard(request):
    return render(request, 'naski/dashboard.html')