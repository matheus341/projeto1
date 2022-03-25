from django.views.generic import  TemplateView
from django.shortcuts import render
from .forms import *



class HomePageView(TemplateView):
    template_name = "home.html"

def index(request):
    return render(request, 'index.html')
