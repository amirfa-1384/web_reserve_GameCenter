from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fieldss = UserCreationForm.Meta.fields + ('idGame', 'phone', )
        fields = ['first_name','last_name','username','idGame','phone','email','password1','password2']

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields