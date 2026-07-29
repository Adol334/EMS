from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

#Get the currently active User model (custom or default)
User = get_user_model()
#Custom registration form based on Django's UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #Use the custom User model
        model = User
        #Fields displayed in the registration form
        fields = ("username",)
    