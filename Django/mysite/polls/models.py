import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    """
    A Question consists of a question and a publication date. 
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # this will represent the object as a string
    # which is much nicer than 'Question object id'
    def __str__(self):
        return self.question_text

    # I think this well tell us if the question was published within
    # the past day or not
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """
    A choice has two fields: the text of the choice and a vote tally. Each choice
    is associated with a question (a question can have many choices, which is
    why we would use a foreign key!).
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # same idea as above, we want to represent our
    # choice text as a string
    def __str__(self):
        return self.choice_text