from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.http import request
from .models import Profile
from backoffice.models import Topic


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileEditionForm(forms.ModelForm):

    interests = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Mes centre d'interet"
    )

    class Meta:
        model = Profile
        fields = ['interests']
