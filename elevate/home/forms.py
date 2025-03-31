from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Thought, Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'content']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
