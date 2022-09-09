# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django import forms
from django.forms import ModelForm
from .models import Testimonial


class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = ('author', 'text', 'active',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '', 'id': 'elder',
                                             'type': 'hidden'}),
        }
