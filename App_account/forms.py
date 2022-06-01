from django import forms
from django.contrib.auth.forms import UserCreationForm
from App_account.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2')
        # this field is User field whice are required field form User abstractbased model please remind it