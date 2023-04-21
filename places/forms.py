from django import forms
from tinymce.widgets import TinyMCE
from .models import Place


class FullDescForm(forms.ModelForm):
    description_long = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Place
        fields = '__all__'