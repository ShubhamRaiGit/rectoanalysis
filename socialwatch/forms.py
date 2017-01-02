from django import forms
from .models import TwitterData

type = (('hashtag', 'hashtag'), ('keyword', 'keyword'))


class TrackerForm(forms.ModelForm):

    class Meta:
        model = TwitterData
        fields = ['keyword']





