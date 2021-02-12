# Django Guide

This guide is created via information from the [Django docs](https://docs.djangoproject.com/en/3.1/). This is simply meant to improve
my understanding of Django.

## Overview

The purpose of Django is to make common web-dev tasks fast and easy.

Django comes with an object relational mapper (a technique for converting types using oop - creates a virtual object database) in which
the db layout can be described with Python code. The data model syntax (models - more to come) offers many rich ways of representing
models. An example:

`
mysite/news/models.py

from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
`

The `makemigrations` command looks at all available models and cretes migrations for whichever don't already exist. The 
`migrate` command runs the migrations and creates tables in the db. This seems pretty useful for changing/creating the db schema.

This offers a free, rich, scalable Python API for any data that needs to be handled. The API is created on the fly too, so no
need for code generation (I'm not quite sure what this means).

Django comes with an admin interface, which allows super sers to add/change/delete/etc objects. This is production ready and the only
catch is that the model needs to be registered in the adming site (this is taken care of in admin.py).

One workflow in Django projects is to create models and get the admin sites up and running as fast as possible to start populating data.
Later the data can be funneled into a GUI to display.

Django allows for customization and flexiblility in URLs. This is managed by a Python module called URLconf. This offers a way to
create a table of contents (of sorts) for the project. The URL paths created map to Python callback functions called views. The paths
serve as a way to capture values from the URLs. So, when someone requests a page, Django runs through each path, **in order**, and stops at the first one that mathces the requested URL (no matches lead to a 404 error). Note, this process is really fast b/c the paths are
compiled into regex expressions at load time (that's pretty neat).

Once a match occurs, Django calls the given view, which is a Python function. Each view gets passed a request object - which contains
metadata - and the values captured in the pattern.

For example, say a user requested the URL "/articles/2005/05/39323", then Django would call the following function:
`news.views.article_detail(request, year=2005, month=5, pk=39323)`.

Django allows you to write your own views. Views must be responsible for doing one of two things: returning an HttpResponse object
containing the content for the request page, or raising an exception such as Http404. Once this responsibility is taken care of,
the details are up to you.

Additionally, Django allows you to design your templates (or connect to a frontend frame work). Django has a template search path,
which minimizes the redundancy among templates. In Django settings, you can specify a list of directories to check for templates
with DIRS. If a template is not found in the first directory, the search continues in the second, and so on.

Django allows variables in templates via double curly braces: `{{your var here}}`. In addition to attribute lookup, dictionary output,
index lookup, and function calls are permitted within the double curly braces. 

Additionally, there is support for the unix pipe character, which serves as a template filter. It is a way to filter the value of a
variable. There is little limit to filtration, as filters can be changed or customly written. Also, there is support for custom 
template tags (`{% code here %}`), which allows for custom Python code behind the scenes (in a sense this kinda replaces the 
javascript that html may use).

Django utilizes template inheritance in the form of something like `{% extends 'template.html' %}`. This allows for modularization
and reduced redundancy. Additionally, you can customize via blocks (i.e. filling in holes in the child template).

You are not forced to use Django's template system if another is preferred. The same applies to Django's db API too. Other db
abstraction layers can be used, read files from somewhere else, it is very flexible. This is because each piece of Django is 
decoupled from the next (so models, views, templates are separate from each other). 

Note, this is just the surface of Django. Some other useful features include: a [caching framework](https://docs.djangoproject.com/en/3.1/topics/cache/), a [syndication framework](https://docs.djangoproject.com/en/3.1/ref/contrib/syndication/), and more attractive automatically generated admin features.