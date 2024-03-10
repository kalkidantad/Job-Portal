from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'autofocus': True}),
    )

    class Meta:
        model = AuthenticationForm
        fields = ['name', 'email', 'password']
