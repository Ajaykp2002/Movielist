from django import forms
from .models import movies
class Form(forms.ModelForm):
    class Meta:
        model=movies
        fields=['Movie_Name','Movie_description','Movie_Year','Movie_img']