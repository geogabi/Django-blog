from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model as user_model
User = user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']