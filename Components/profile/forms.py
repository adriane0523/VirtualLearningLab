from django import forms
from .models import Profile
import django.core.validators
from datetime import datetime

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'birthdate',)

    birthdate = forms.DateField(
        label='Birthdate',
        widget=forms.widgets.SelectDateWidget(
            years=range(1920, datetime.now().year),
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ),
    )