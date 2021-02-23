# Tutorial

## Startup

To get the version of Django run: `python3 -m django --version`.

To start a new Django project run: `django-admin startproject name_of_project`. Note, the name of the project must avoid the name of
built-in Python or Django components.

## Structure

Django does not put code under the Web server's document root, because of the potential risk where people may be able to view your code. 
The code can live in some directory outside of the document root.

Here is what the `startproject` command created:

```
name_of_project/
    manage.py
    name_of_project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

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

**name_of_project/asgi.py** is an entry point for ASGI compatible web servers to serve your project.

**name_of_project/wsgi.py** is an entry point for WSGI compatible web serve to serve your project.

## Creating an app

After the environment of the project is set up, the fun begins! Each application you write in Django consists of a Python package that
follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so the
focus can be on writing the code.

Apps can live anywhere in the Python path. To create an app, head to the directory in which you would like to place it in and
run the following command: `python manage.py startapp name_of_app`. This will create a directory of the following structure:

```
name_of_app/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### Projects vs app

An app is a web application that does something (e.g. a Weblog system, a db of public records, or a small poll app). A project is a 
collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

## Path()

The `path()` function is passed four arguments, two required: **route** and **view**, and two optional: **kwargs** and **name**. 

The **route** is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in `urlpatterns` 
and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches. Patterns don't 
search **GET** and **POST** parameters, or the domain name. 

When Django finds a matching patterns, it calls teh specified **view** function with an `HttpRequest` object as the first argument and 
any "captured" values from the route as keyword arguments.

**kwargs** are arbitrary keyword arguments that can be passed in a dictionary to the target view.

Naming the URL allows you to refer to it unambigously from elsewhere in Django, especially from within templates. This powerful feature
allows you to make global changes to the URL patterns of your project while only touching a single file.

## Command Notes

By default, the `runserver` command starts the development server on the internal IP at port 8000. If you want to change the server's
port, pass it as a command line argument like so: 

`python3 manage.py runserver port_num`

If you want to change the server's IP, pass it along with the port like so:

`python3 manage.py runserver ip_num:port_num`

The server automatically reloads Python code for each request as needed (no need to restart while coding!).

## Good to Know

**Never** deploya site into production with `DEBUG` turn on.
