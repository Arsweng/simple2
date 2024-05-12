from django import forms
from django.contrib.auth.models import User

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10,strip=True, required=True)
    password = forms.CharField(max_length=10,strip=True, required=True,
    widget=forms.PasswordInput(attrs={'input_type':'password'})
    )
    class Meta:
        model = User
        fields =['username','password']
