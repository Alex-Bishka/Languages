from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # this will save the data from a valid form
            # next step is to log in the user
            return redirect('articles:list')
    else:
        # get request case
        form = UserCreationForm()  # creates a new instance of the form

    # the third parameter is a dictionary of data we can pass in
    # this data is passed into the html template listed in our second
    # parameter
    return render(request, 'accounts/signup.html', {'form':form})  
