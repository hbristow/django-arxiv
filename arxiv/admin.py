from django import forms
from django.conf import settings
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from arxiv import models

class MailServerForm(forms.ModelForm):
    class Meta:
        model = models.MailServer
        if settings.EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend':
            fields = ('domain', 'name', 'email', 'host', 'port', 'username', 'password', 'tls', 'ssl')
            widgets = {'password': forms.PasswordInput(render_value=True)}
        else:
            fields = ('domain', 'name', 'email')

    def clean(self):
        fields = super(MailServerForm, self).clean()
        tls = fields.get('tls')
        ssl = fields.get('ssl')
        if tls and ssl:
            raise forms.ValidationError('TLS and SSL are mutually exclusive. Please set only one.')
        return fields

class MailServerAdmin(SingletonModelAdmin):
    form = MailServerForm

# Only make MailServer visible
#   - Subjects and Timezones are not editable
#   - Subscribers are private
admin.site.register(models.MailServer, MailServerAdmin)
