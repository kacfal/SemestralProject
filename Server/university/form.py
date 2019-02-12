from django import forms
from .models import University


class UniversityModelForm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'
