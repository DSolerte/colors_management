from django.forms import ModelForm

from management.models import Color


# creating a form
class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'red', 'green', 'blue']


class SearchColorForm(ModelForm):
    class Meta:
        model = Color
        fields = ['name']
