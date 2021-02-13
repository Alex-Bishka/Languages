# Django Guide

This guide is created via information from the [Django docs](https://docs.djangoproject.com/en/3.1/). This is simply meant to improve
my understanding of Django.

## Overview

The purpose of Django is to make common web-dev tasks fast and easy.

### Models

Django comes with an object relational mapper (a technique for converting types using oop - creates a virtual object database) in which
the db layout can be described with Python code. The data model syntax (models - more to come) offers many rich ways of representing
models. 

**An example:**

```
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
```

The `makemigrations` command looks at all available models and cretes migrations for whichever don't already exist. The 
`migrate` command runs the migrations and creates tables in the db. This seems pretty useful for changing/creating the db schema.

This offers a free, rich, scalable Python API for any data that needs to be handled. The API is created on the fly too, so no
need for code generation (I'm not quite sure what this means).

### Admin

Django comes with an admin interface, which allows super sers to add/change/delete/etc objects. This is production ready and the only
catch is that the model needs to be registered in the adming site (this is taken care of in admin.py).

One workflow in Django projects is to create models and get the admin sites up and running as fast as possible to start populating data.
Later the data can be funneled into a GUI to display.

### URLs

Django allows for customization and flexiblility in URLs. This is managed by a Python module called URLconf. This offers a way to
create a table of contents (of sorts) for the project. The URL paths created map to Python callback functions called views. The paths
serve as a way to capture values from the URLs. So, when someone requests a page, Django runs through each path, **in order**, and stops at the first one that mathces the requested URL (no matches lead to a 404 error). Note, this process is really fast b/c the paths are
compiled into regex expressions at load time (that's pretty neat).

### Views

Once a match occurs, Django calls the given view, which is a Python function. Each view gets passed a request object - which contains
metadata - and the values captured in the pattern.

For example, say a user requested the URL "/articles/2005/05/39323", then Django would call the following function:
`news.views.article_detail(request, year=2005, month=5, pk=39323)`.

Django allows you to write your own views. Views must be responsible for doing one of two things: returning an HttpResponse object
containing the content for the request page, or raising an exception such as Http404. Once this responsibility is taken care of,
the details are up to you.

### Templates

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

### Continuation

Note, this is just the surface of Django. Some other useful features include: a [caching framework](https://docs.djangoproject.com/en/3.1/topics/cache/), a [syndication framework](https://docs.djangoproject.com/en/3.1/ref/contrib/syndication/), and more attractive automatically generated admin features.






## Models

A model is the single, definitive source of information about your data. It contains essential fields and behaviors of the data
you're storing. Generally, each model maps to a single db table.

Simply put, each model is a Python class that subclasses django.db.models.Model, each attribute of the model represents a db field,
and with all of this Django provides an automatically generated db access API.

Properties of a the model class are referred to as fields. Each field is specified as a class attribute, and each attribute mps
to a database column.

**Example (model then representation of model in db table):**

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

```
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```

The name of the table comes from model metadata, but can be overriden. The id field is added automatically, but can also
be overriden. `CREATE TABLE` SQL is formatted using PostgresSQL syntax, but it's worth noting Django uses SQL tailored to the db backend
specified in the settings file.

Once you have defined your models, Django needs to be told that those models will used. This is done by editing the settings file
and changing the `INSTALLED_APPS` setting to add the name of the module that contains the models.py file. 

When creating new apps and adding them to `INSTALLED_APPS` make sure to run `manage.py migrate` and then `manage.py makemigrations`.

Fields are the most important and only required part of a model. They serve as the list of db fields. Fields are specified
by class attributes. Avoid using field names such as `clean`, `save`, or `delete` as they could conflict with the models API.

Django uses fields to determine a few things: the column type (this tells the db what kind of data to store), the default html
widget to use when rendering a form field, and the minimal validation requirements. Django has lots of built-in field types,
which can be found [here](https://docs.djangoproject.com/en/3.1/ref/models/fields/#model-field-types). You can also write custom
fields if needed.

Each field takes in a certain set of field-specifc arguments. For example, the `CharField` will require a `max_length` argument.
Django can allow empty values to be stored in the db, as well as blank values (blank is different from null), and even choices
(which will create a form with select boxes). There are also arguments like default, help_text (extra help to be displayed on a
widget), etc. A verbose name for the field can be passed in as an optional first argument. 

The power of relational databases lies in relating tables to each other. Django offers ways to define the three most common types
of db relationships: 1) **many-to-one**, 2) **many-to-many**, and 3) **one-to-one**.

For a **many-to-one** relationship, use `django.db.models.ForeignKey`. You use it like any other `Field` typeL by including it
as a class attribute of your model. `ForeignKey` requires a positional argument: the class to which the model is related.

**An example:**

```
from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...
```

The car model has a manufacturer. However, that manufacturer makes multiple cars, but each car only has one manufacturer. It is
suggested that the name of a `ForeignKey` field be the name of model, lowercase.

To define a **many-to-many** relationship, use `ManyToManyField`. You use it just like any other `Field` type, by including it as
a class attribute of your model. Similar to `ForeignKey`, the `ManyToManyField` requires the class to which the model is related
as an argument.

**An example:**

```
from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
```

A pizza can have multiple toppings and a topping can be on multiple pizzas. It is suggested that the name of a `ManyToManyField` be
a plural describing the set of related model objects. It does not matter which model contains the `ManyToManyField`, but it should
only be put in one of the models, not both! Generally, it should be put in the object that's going to be edited on a form. Extra 
details may be added to this field if the data needs to be associated b/w two models.

To define a `OneToOneField` you use it like any other `Field` type: by including it as a class attribute of your model. This is most
useful on the primary key of an object that extends another object in some way.

**Models can be related across files - make sure to namespace!**

Define custom methods on a model to add custon *row_level* functionality to your objects. Manager methods are intended to do
*table-wide* things, model methods should act on a particular model instance. This is valuable for keeping business logic in
one place, the model.

**An example:**

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
```

This model has a couple of custom methods. The last method in this example is a property. You are free to override pre-defined
methods (and ones you write) to alter behavior. Just remember to call the superclass to get the orginal method to run.



## Views

A clean, elegant URL scheme is an important detail in a strong project. Django allows you to design URLs however you want, with no
framework limitations. To design URLs for a project, you create a Python module informally called a URLconf. This module is pure
Python code and is a mapping b/w URL path expressions to Python functions (views). This mapping can be short, long, reference other
mappings, etc. Since it is pure Python code, it can be constructed dynamically.

When a user requests a page from a Django site, this is the algorithm the system follows to determine which Python code to 
execute:

    1.  Django determines the root URLconf module to use. Ordinarily, this is the value of the `ROOT_URLCONF` setting, but if the
        incoming `HttpRequest` object has a `urlconf` attribute (set by middleware), its value will be used in place of the
        `ROOT_URLCONF` setting.
    2.  Django loads that Python module and looks for the variable `urlpatterns`. This should be a sequence of `django.urls.path()`
        and/or `django.urls.re_path()` instances.
    3.  Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL, matching against
        `path_info`.
    4.  Once one of the URL pattern matches, Django imports and calls the given view, which is a Python function (or a class based
        view). The view gets passed the following arguments:
            - An instances of `HttpRequest`
            - If the matched URL pattern contained no named groups, then the matches from the regular expression are provided as
              positional arguments
            - The keyword arguments made up of any named parts matched by the path expression that are provided, overriden by and
              arguemnets specified in the optional `kwargs` argument to `django.urls.path()` or `django.urls.re_prath()`
    5.  If no URL pattern matches, or if an exception is raised during any point in this process, Django invokes an appropriate error
        handling view.

Note, to capture a value from the URL, use angle brackets. You can create your own converters, or use regular expressions, just make
sure you use `re_path()` instead of `path()`.

Also note, the URLconf doesn't look at the request method. In other words, all request methods - **POST**, **GET**, **HEAD**, etc - will
be routed to the same function for the same URL (in other words, our view will handle request methods).

A convenient trick is to specify default parameters for your views' arguments.

The performance of this is blazingly fast because each regex in `urlpatterns` is complied the first time it's accessed. Note that
`urlpatterns` should be a sequence of `path()` and/or `re_path()` instances. Paths can "include" other URLconf modules. This "roots"
a set of URLs below other ones. This is done by using `include()`. Pretty useful for adding URLs/URLconfs for other apps within
the Django process. An included URLconf still receives caputred parameters from the parent URLconf.

You can include a `name` parameter within a url path, which can then be used in Python code or in templates. This saves a lot of
work, as urls can change freely while the rest of the code stays the same.

URL namespaces are useful for maintaining organzied code. Specifically, instance namespaces are extremely useful. Namespaced URLs
are specified using the **:** operator. Namespaces can be nested if needed. Namespacing can also be applied to URLconfs. In this case,
the `include()` a string must be passed in the form `module_name.urls`. Alternatively, a new url pattern can be used.

## Template Layer

## Forms

## Development Process

## The admin

## Security