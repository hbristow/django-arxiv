import uuid
import pytz
from solo.models import SingletonModel
from django.core import mail
from django.core.mail.backends import smtp
from django.db import models

# ----------------------------------------------------------------------------
# Mail Server Configuration
# ----------------------------------------------------------------------------
class MailServer(SingletonModel):
    """App configuration model"""
    email = models.EmailField('Email Address', max_length=128)
    host  = models.CharField('SMTP Hostname', max_length=64)
    port  = models.IntegerField('Port Number', default=25)
    username = models.CharField('Username', max_length=64)
    password = models.CharField('Password', max_length=64)
    tls = models.BooleanField('TLS', default=False)
    ssl = models.BooleanField('SSL', default=False)

    class Meta:
        verbose_name = 'Mail Server Configuration'

    def get_connection(self):
        return mail.get_connection(
            # backend=settings.EMAIL_BACKEND,
            host=self.host, port=self.port,
            username=self.username, password=self.password,
            use_tls=self.tls, use_ssl=self.ssl)

    def send_mail(self, subject, message, recipients, **kwargs):
        """Send email from the mail server. See django.core.mail.send_mail"""
        return mail.send_mail(subject, '', self.email, recipients,
            html_message=message, connection=self.get_connection(),
            **kwargs)


# ----------------------------------------------------------------------------
# Subscribers
# ----------------------------------------------------------------------------
class Subject(models.Model):
    """Representation of a subject area"""
    name = models.CharField('Name', max_length=128)
    cat = models.CharField('Category Code', max_length=64)

    def __unicode__(self):
        """Describe a subject by its name and category code"""
        return '{cat} ({name})'.format(cat=self.cat, name=self.name)

class Subscriber(models.Model):
    """Feed subscriber"""
    email = models.EmailField('Email Address', max_length=128)
    uuid = models.CharField('Universal Identifier', max_length=32, editable=False, blank=True)
    timezone = models.CharField('Timezone', max_length=64,
        choices=((timezone,timezone) for timezone in pytz.all_timezones))
    subjects = models.ManyToManyField(Subject)

    def save(self, *args, **kwargs):
        """Generate a unique identifier for the subscriber on save"""
        self.uuid = uuid.uuid1().hex
        super(Subscriber, self).save(*args, **kwargs)

    def __unicode__(self):
        """Describe the subscriber by their email address"""
        return self.email
