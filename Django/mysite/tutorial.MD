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

### App Details

All Django apps that are active will be held within the `INSTALLED_APPS` list, contained in `settings.py`.

By default Django comes with a bunch of apps. These pre-installed apps help with the admin site, authenticaion, content types,
sessions, messages, and static files.

### Projects vs App

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

## Database setup

This will largely come from part two of the django tutorial. Django has SQLite baked into it, making it an easy choice for a project to
use. SQLite is included in Python, so there is no need to tinker with anything. However, for a real project, a more scalable db may
serve as a better choice.

If you wish to switch to another db, install the appropriate [db bindings](https://docs.djangoproject.com/en/3.1/topics/install/#database-installation). 
Additionally, make sure to change the following keys in the `DATABESES` 'default' item to match your db connection settings (i.e. 
the `ENGINE` and `NAME`). For a non-SQLite db, additional settings like `USER`, `PASSWORD`, and `HOST` must be added. More details
can be found [here](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-DATABASES).

## Creating Models

Models serve as our db layout, with some extra metadata. In Django, a model is the single, definitie source of truth about your data. It
contains the essential fields and behaviors of the data you're storing.

Models contain a number of class variables, each of whic represents a db field in the model. Each field is represented by an instance
of a `Field` class. This will tell Django what type of data each field holds. The name if each `Field` instance is the field's name.
This value can be used in the python code, and will be used as a column name for the database.

Creating a model for an app will all Django to create a db schema for that app and create a Python db-access API for accesssing the
objects within the model. Migrations are very powerful and let you change your models over time, as you develop your project, without
the need to delete your db or tables and make new ones - it specializes in upgrading your db live, without losing data.

Three step guide to making model changes:
    1. Change your models in `model.py`
    2. Run `python3 manage.py makemigrations` to create migrations for those changes
    3. Run `python3 manage.py migrate` to apply those changes to the db

## Django Admin

Django provies an admin interface for models. It's a great way for site managers to manage models. 

First, we will need to create a user who can login to the admin site. This is done by running `python manage.py createsuperuser`. Then,
enter your desired username, email address, and password (note: **username=alex**, skipped email, **password=123456**).

We can then go to the admin page (after running the server) by going [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Groups
and users will be in the admin site by default.

In order for apps to appear in the admin site, we need to alert the admin of the model objects we want to store. To do this, we will
need to register the classes within a model on the `admin.py` file of an app.

## Views

A view is a "type" of web page in your Django application that generally serves a specific function and has a specific template. For
example, in a blog application, you might have the following views:
    - Blog homepage (displays the latest few entries)
    - Entry "detail" page (permalink page for single entry)
    - Year-based archive page (displays all months with entries in given year)
    - Month-based archive page (display all the day with entries in given month)
    - Day-based archive page (displays all entries in the given day)
    - Comment action (handles postin comments to a given entry)

In Django, web pages and other content are delivered by views. Each view si represented by a Python function (or method, in the case of
class-based views). Django will choose a view by examining the URL that is requested. To get a from a URL to a view, Django utilizes
URLconfs (maps URL patterns to views).

Once a view is created, it needs to be wired into the appropriate app url file via a call to `path()`.

## Command Notes

By default, the `runserver` command starts the development server on the internal IP at port 8000. If you want to change the server's
port, pass it as a command line argument like so: 

`python3 manage.py runserver port_num`

If you want to change the server's IP, pass it along with the port like so:

`python3 manage.py runserver ip_num:port_num`

The server automatically reloads Python code for each request as needed (no need to restart while coding!).

The `migrate` commaned can be called like so:

`python manage.py migrate`

It looks at the installed apps setting and creates any necessary db tables according to the db settings in the `settings.py` file and
the db migrations shipped with the app.

The `makemigrations` command can be run like so:

`python3 manage.py makemigrations app_name`

By running `makemigrations`, you are telling Django that you've made some changes to your models, and you would like the changes to be 
sotred as a migration.

The `check` command is very useful. It will check to see if there are any problems in your project without making migrations or touching
the db. The full command is `python3 manage.py check`.

Django also comes with an interactive Python shell that will let you play aorund with the free API Django gives you. Simply invoke the 
command `python3 manage.py shell`. For more information on what you can do in the shell, [this](https://docs.djangoproject.com/en/3.1/ref/models/relations/) is a good start. As well as [this](https://docs.djangoproject.com/en/3.1/topics/db/queries/#field-lookups-intro) for fields. This [link](https://docs.djangoproject.com/en/3.1/topics/db/queries/) offers detials on the entire API.

## Good to Know

**Never** deploya site into production with `DEBUG` turn on.
