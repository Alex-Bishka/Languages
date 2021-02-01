from django.http import HttpResponse
from django.shortcuts import render # allows us to render a html template in the browser

"""
These are the functions that will fire when a user visits a 
certain url
"""

def home(request):
    """
    request parameter is the request object given to us inside this
    function when a user visits the about url

    render will allow us to display html files
    """
    return render(request, 'home.html')

def about(request):
    """
    request parameter is the request object given to us inside this
    function when a user visits the about url

    render will allow us to display html files
    """
    return render(request, 'about.html')