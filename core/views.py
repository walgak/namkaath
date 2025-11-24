from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'get_started.html')