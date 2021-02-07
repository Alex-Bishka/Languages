from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    form = UserCreationForm()  # creates a new instance of the form

    # the third parameter is a dictionary of data we can pass in
    # this data is passed into the html template listed in our second
    # parameter
    return render(request, 'accounts/signup.html', {'form':form})  
