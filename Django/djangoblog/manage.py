#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""
This controls a lot of things for us like:
    1) spin up a server 
        -this can be done with the following command: 'python3 manage.py runserver'
    2) control migrations
        -the command for this is: 'python3 manage.py migrate'
            -this will migrate models that django created to the DB
            -re-run for new apps w/models and migration files
                -to migrate new apps w/modes run 'python3 manage.py makemigrations'
                -followed by 'python3 manage.py migrate'
    3) communicate with a db
        -some useful commands:
            -from location_of_models import class_name (if in interactive shell)
                i.e. from articles.models import Article
            -class_name.objects.all() (lists all articles)
            -how to create an instance:
                instance_name = class_name()
            -instance.property = value_to_set_property
            -instance.save() (stores in DB)
    4) create an app (apps are separate parts of a djano project, they modularize the project)
        -the command for this is 'python3 mangage.py startapp app_name'
        -note, in django the 'app_name' is typical plural
        -views are rendered w/in apps
        -url files are separate within each individual app
        -don't forget to add the app within the 'INSTALLED_APPS' list in settings.py in the main folder
    5) open an interactive shell
        -the command: 'python3 manage.py shell'
        -not quite sure how this differes from ipython3...
        -in this shell we can interact with the DB
    6) set-up django admin area
        -to create a super user:
            'python3 manage.py createsuperuser'
            -this will then prompt you for:
                Username: alex (for this tutorial) 
                Email addr (can be left blank):
                Password: test1234 (for this tutorial)
            -a superuser will have acess to the admin area
        -the admin area is an area for site admins to control the
         contents of the website or the contents of the DBS
        -we can create instances of models such as articles or something else
        -we can control users of our websites
        -and a lot more!

Django project come automatically configured with sqlite (store our data for us)
    -we can change the db down the line
"""

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoblog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
