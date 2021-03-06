from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # this will save the data from a valid form and gives us the user
            # log in the user
            login(request, user)

            # redirect the user after logging them in
            return redirect('articles:list')
    else:
        # get request case
        form = UserCreationForm()  # creates a new instance of the form

    # the third parameter is a dictionary of data we can pass in
    # this data is passed into the html template listed in our second
    # parameter
    return render(request, 'accounts/signup.html', {'form':form})  

def login_view(request):
    if request.method == "POST":
        # we have to specify the data parameter in this case
        # b/c it is not naturally the first param in the method
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)

            # send user to the appropriate page
            # if there is a next parameter in the 
            # login url
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                # otherwise send them to the articles list
                return redirect('articles:list')
    else:
        # get request
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == "POST":
        # don't need to pass in the current user, as we are already
        # logged in, and Django knows this
        logout(request)
        return redirect('articles:list')