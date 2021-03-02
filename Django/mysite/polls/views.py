from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
#from django.template import loader  # no longer needed b/c of render shortcut

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    """
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """
    """
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    """
    """
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    """
    This function will increase the number of votes a selected
    question have, if it exists, and then redirect us to the results
    page. If said question fails, we are given a 404 error!

    Reverse will take us to the view specified by arg1 along with the
    variable portion of the url specified by arg2.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        # this will obtain the id of the selected choice as a string
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # error message if choice isn't given
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # redirected to this url - always return a redirect after successfully
        # dealing with POST data - prevents data from being posted twice if the
        # user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


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
