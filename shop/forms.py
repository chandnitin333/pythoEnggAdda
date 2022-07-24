from dataclasses import field
from pyexpat import model
from django import forms
from .models import BookTable


class BookTableFrom(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = "__all__"
    
   