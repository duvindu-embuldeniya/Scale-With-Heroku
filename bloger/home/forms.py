from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import Profile, Blog
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email has already taken!")
        return email




# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Get the current user from the form instance
        current_user = self.instance

        # Check if email exists and doesn't belong to the current user
        if User.objects.filter(email=email).exclude(pk=current_user.pk).exists():
            raise ValidationError("This email is already in use by another account.")
        return email




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['f_name', 'l_name', 'image']





class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']