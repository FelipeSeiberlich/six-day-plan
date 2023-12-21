from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def questionnaire(request):
    return HttpResponse("Please fill out this Health form.")
