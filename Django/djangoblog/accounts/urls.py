from django.urls import path
from . import views # these two imports must be done for every urls.py file

# namespacing:
app_name = 'accounts'

# after creating these urls here, don't forget to include them in the 
# root urls file!
urlpatterns = [
    path('signup/', views.signup_view, name="signup")
]

