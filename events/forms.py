from django import forms
from .models import Unregistered_user, Comments

class Unregistered_user_form(forms.ModelForm):
  class Meta:
    model = Unregistered_user
    fields = ['first_name', 'last_name', 'email']


class Comments_form(forms.ModelForm):
  class Meta:
    model = Comments
    fields = ['comments']