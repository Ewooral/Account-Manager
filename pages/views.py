from django.shortcuts import render
from django.http import HttpResponse

''' 
It should be noted that class-based view is prefered over generic view
'''


def home(request):
    return render(request, 'pages/home.html', {"title": "Home"})


def portfolio(request):
    return render(request, 'pages/portfolio.html', {"title": "Portfolio"})


def about(request):
    return render(request, 'pages/about.html', {"title": "about"})


def abouts(request):
    return render(request, 'pages/abouts.html', {"title": "abouts"})



def contact(request):
    return render(request, 'pages/contact.html', {"title": "contact"})


def dashboard(request):
    return render(request, 'pages/dashboard.html', {"title": "Dashboard"})


def ranking(request):
    return render(request, 'pages/ranking.html', {"title": "Ranking"})



# Create your views here.
