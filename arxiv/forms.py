from django import forms
from arxiv import models

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        fields = ('email', 'subjects', 'timezone')
        widgets = {
            'email': forms.EmailInput(attrs={'required': True}),
            'subjects': forms.SelectMultiple(attrs={'required': True}),
            'timezone': forms.Select(attrs={'required': True})
        }
