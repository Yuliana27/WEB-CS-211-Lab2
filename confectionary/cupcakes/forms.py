from django import forms
from .models import Calls

class CallsForm(forms.ModelForm):
    class Meta:
        model = Calls
        fields = ('name', 'phone')