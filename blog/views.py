from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gym_blog(request):
    return HttpResponse("This Blog is awesome!")