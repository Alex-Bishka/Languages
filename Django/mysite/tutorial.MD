# Tutorial

## Startup

To get the version of Django run: `python3 -m django --version`.

To start a new Django project run: `django-admin startproject name_of_project`. Note, the name of the project must avoid the name of
built-in Python or Django components.

## Structure

Django does not put code under the Web server's document root, because of the potential risk where people may be able to view your code. 
The code can live in some directory outside of the document root.

Here is what the `startproject` command created:

`
name_of_project/
    manage.py
    name_of_project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
`

The outer **name_of_project/** directory serves as a container for the project. The name of this folder does not matter to Django, and it
can actually be renamed.

**manage.py** is a command line utility that lets you interact with this Django project in various ways. More details can be found
[here](https://docs.djangoproject.com/en/3.1/ref/django-admin/). Note, this will be covered in the guide.MD file that I am working on.

The inner **name_of_project/** directory is the actual Python package for the project. Its name is the Python package name you'll need to
use to import anything inside of it (e. g. **name_of_project.urls**).

**name_of_project/__init__.py** is an empty file that tells Python that this directory shold be considered a Python package. For more 
information on packages, read on [here](https://docs.python.org/3/tutorial/modules.html#tut-packages). As a quick note, packages are a 
way of structuring Python's module namespace.

**name_of_project/settings.py** serves as the settings/configuration file for the Django project. More information of how the settings 
work can be found [here](https://docs.djangoproject.com/en/3.1/topics/settings/).

**name_of_project/urls.py** provides the URL declarations for this Django project, a "table of contents" of your Django-powered site.
For more details on how URLS work in Django, read [here](https://docs.djangoproject.com/en/3.1/topics/http/urls/).
