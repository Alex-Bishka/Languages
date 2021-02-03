from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.

"""
note templates for the articles app will be kept within
the articles folder

we typically add another folder within this local template
folder that is the name of the app - the purpose for this
is to 'namespace' templates so they will not be confused
will global templates (or other ones)

global templates (that the entire app needs) will be kept
in the templates folder in the root dir
"""

def article_list(request):
    """
    responsible for rendering our list of articles, specifically
    the template defined by the second arguement and the data
    (in the third arg) that feeds into the template
    """
    # the data we will send to the template
    articles = Article.objects.all().order_by('date')

    return render(request, 'articles/article_list.html', {'articles': articles}) # here is where namespacing is nice

def article_detail(request, slug):
    """
    """
    return HttpResponse(slug)