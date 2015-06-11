from django.core.management.base import BaseCommand, CommandError

from arxiv import models

class Command(BaseCommand):
    """Send a test email to verify mail server configuration"""

    def add_arguments(self, parser):
        parser.add_argument('recipient')

    def handle(self, *args, **kwargs):
        mail_server = models.MailServer.get_solo()
        recipient = kwargs['recipient']
        mail_server.send_mail('arXiv test', '', [recipient])
