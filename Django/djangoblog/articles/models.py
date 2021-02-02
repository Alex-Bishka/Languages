from django.db import models

# Create your models here.

"""
This file is automatically generated with apps

model files serve as a way to get records from a DB

A model is represented by a class in Django
    -by convention the name of the class starts with
     a capital letter

model filed types
    -will give Django an idea of what is stored (in terms of
     data type)
    -a charField is a small amount of text
    -a textField is a large amount of text

After a model is creating, it must be migrated to the DB
so that the DB is aware of the existence of the model - the
DB will then be aware to create the table that the model 
has described in the class

You first need to create a migration file before migrating. This
will track the changes that occur to the model file. This will be
responsible for updating the DB.

To create the migration file use the following command:
    python3 manage.py makemigrations
"""
class Article(models.Model):
    # class properties
    title = models.CharField(max_length=100) 
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # automatically populates this field with now time
    # add in thumbnail later
    # add in author later

    # self will be the instance of the article
    def __str__(self):
        """
        This should return the title of an instance of an Article
        when we get the article objects from the server.

        So Article.objects.all() will return the title of the articles
        rather than something useless like 'Article object (1)'
        """
        return self.title