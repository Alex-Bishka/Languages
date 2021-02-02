"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

"""
This is where we control routes/how we send users to different pages

urls.py has the following jobs:
    -look at the request URL from the browser
    -decide which function to fire in views.py
    -views.py will then run the function, which will control what the user
     sees when they visit that url in the browser (i.e some html template)

need to create a url that will include urls from other apps in order
to register the url(s) of other apps this is done by using the following 
code:
            'path(name_of_route, include(name_of_app.urls))
    -note that name_of_route and name_of_app.urls must be strings
    -also note that the name_of_route should probably something like app_name/
     such that future urls created in the app will extend off of app_name/
     (i.e a url of about in the new app will then be app_name/about/)
"""

urlpatterns = [
    path('admin/', admin.site.urls), # created and shipped by Django for you (our admin section)
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('articles/', include("articles.urls")), # will include urls from our articles app
]
