from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from user.models import User




class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    class Meta:
        model = User
        fields = ('username', 'email')