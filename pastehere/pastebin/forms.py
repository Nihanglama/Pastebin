from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

from django.forms import ModelForm

class UserRegister(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class Update_profile(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']