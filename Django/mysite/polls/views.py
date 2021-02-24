from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
#from django.template import loader  # no longer needed b/c of render shortcut

from .models import Question
# Create your views here.

def index(request):
    """
    index will display the latest 5 poll questions in the system, separated by commans,
    according to the publication date.

    render takes the request as its first arg, a template name as the second,
    and a dictionary as the optional third. It returns an HttpResponse object
    of the given template rendered with the given context.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """
    Returns a simple template response.

    get_object_or_404 takes in a Django model as its first arg and
    an arbitrary number of keywords to pss to the get part of the model
    manager. A 404 error is raised if the object does not exist.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    Returns a simple template response.
    """
    response = "You're looking at the results of questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """
    Returns a simple template response.
    """
    return HttpResponse("You're voting on question %s." % question_id)


#################################################################################################################3
### Previous versions of functions below!
#################################################################################################################3

#def index(request):
    #"""
    #index will display the latest 5 poll questions in the system, separated by commans,
    #according to the publication date.
    #"""
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {
        #'latest_question_list': latest_question_list
    #}
    # httpresponse is common, but render is a shortcut!
    #return HttpResponse(template.render(context, request))


#def index(request):
    #"""
    #The simplest view possible in Django
    #"""
    #return HttpResponse("Hello world! You're at the polls index!")

# one way of writing a 404 error
#def detail(request, question_id):
    #"""
    #Returns a simple template response.
    #"""
    #try:
        #question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
        #raise Http404("Question does not exist!")
    #return render(request, 'polls/detail.html', {'question': question})
