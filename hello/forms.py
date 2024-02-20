from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateUserForm (UserCreationForm):
        class Meta:
           model = User
           fields =['username','email','password1','password2']



from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'card_number', 'phone_number',]  # Добавьте другие поля, если необходимо