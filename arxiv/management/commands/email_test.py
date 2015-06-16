from django.core.management.base import BaseCommand, CommandError

from arxiv import models, tasks

class Command(BaseCommand):
    """Send a test email to verify mail server configuration"""

    def add_arguments(self, parser):
        parser.add_argument('recipient')

    def handle(self, *args, **kwargs):
        # make a temporary subscriber
        subscriber = models.Subscriber.objects.create(email=kwargs['recipient'], timezone='UTC')
        try:
            subscriber.subjects = models.Subject.objects.all()
            tasks.email_feed(subscriber)
        finally:
            subscriber.delete()
