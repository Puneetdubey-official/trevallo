from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class loginform(forms.ModelForm):
	name = forms.CharField(label='Enter username', widget=forms.TextInput(
		attrs={'class':'form-control', 'placeholder':'Enter Name Here PLZ', 'id':'d1'}), required=True, max_length=100)
	password = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)

	class Meta():
		model = User
		fields = ['username', 'password']

class SignupForm(UserCreationForm):
	email = forms.EmailField(max_length=200)


	class meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

