from django.urls import path, re_path
from . import views

"""
We still need to import views and the urlpatterns.

re_path() will allow the use of regular expressions (path() does not). 
"""

# name spacing our url file
app_name = 'articles'

# create must come above the slug, or else django will think that create is a slug
# re_path will extend the url to the name - or rather slug - of the article
urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]