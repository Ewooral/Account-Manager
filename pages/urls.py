from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('portfolio/', views.portfolio, name='portfolio-page'),
    path('dashboard/', views.dashboard, name='dashboard-page'),
    path('ranking/', views.ranking, name='ranking-page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('abouts/', views.abouts, name='abouts'),
]
