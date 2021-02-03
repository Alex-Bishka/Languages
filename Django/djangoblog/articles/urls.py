from django.urls import path, re_path
from . import views

"""
We still need to import views and the urlpatterns.

re_path() will allow the use of regular expressions (path() does not). 
"""

# name spacing our url file
app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    # this will extend the url to the name - or rather slug - of the article
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]