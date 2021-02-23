from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    The simplest view possible in Django
    """
    return HttpResponse("Hello world! You're at the polls index!")
