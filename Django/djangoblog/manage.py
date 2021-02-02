#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""
This controls a lot of things for us like:
    -spin up a server 
        -this can be done with the following command: 'python3 manage.py runserver'
    -control migrations
        -the command for this is: 'python3 manage.py migrate'
            -this will migrate models that django created to the DB
            -re-run for new apps w/models and migration files
                -to migrate new apps w/modes run 'python3 manage.py makemigrations'
    -enter an interactive shell
    -communicate with a db
    -create an app (apps are separate parts of a djano project, they modularize the project)
        -the command for this is 'python3 mangage.py startapp app_name'
        -note, in django the 'app_name' is typical plural
        -views are rendered w/in apps
        -url files are separate within each individual app
    -open an interactive shell
        -the command: 'python3 manage.py shell'
        -not quite sure how this differes from ipython3...
        -in this shell we can interact with the DB
        -some useful commands:
            -from location_of_models import class_name
                i.e. from articles.models import Article
            -class_name.objects.all() (lists all articles)
            -how to create an instance:
                instance_name = class_name()
            -instance.property = value_to_set_property
            -instance.save() (stores in DB)

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
