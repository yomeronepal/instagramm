from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields =['username','email','password1','password2']

class CreatePostForm(ModelForm):
    class Meta:
        model= Post
        fields=['text','post_image']

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','image']