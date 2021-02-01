from django.urls import path
from . import views

"""
We still need to import views and the urlpatterns.
"""

urlpatterns = [
    path('', views.article_list),
]