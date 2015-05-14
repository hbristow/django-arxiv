from django import forms
from arxiv import models

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        fields = ('email', 'subjects', 'timezone')
