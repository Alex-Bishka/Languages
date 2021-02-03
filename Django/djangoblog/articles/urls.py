from django.urls import path, re_path
from . import views

"""
We still need to import views and the urlpatterns.

re_path() will allow the use of regular expressions (path() does not). 
"""

urlpatterns = [
    path('', views.article_list),
    # this will extend the url to the name - or rather slug - of the article
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail),
]