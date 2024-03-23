from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Adoption


class AdoptionForm(forms.ModelForm):

    class Meta:
        model = Adoption
        fields = [
            "title",
            "name",
            "animal_type",
            "age",
            "color",
            "gender",
            "image",
            "description"
        ]

        description = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 10})
        }

        labels = {
            "title": "Ad Title",
            "name": "Animal Name",
            "animal_type": "Species",
            "age": "Age",
            "color": "Colour",
            "gender": "Gender", 
            "image": "Animal Image",
            "description": "Description"
        }
