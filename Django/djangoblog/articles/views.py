from django.shortcuts import render

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
    """
    return render(request, 'articles/article_list.html') # here is where namespacing is nice