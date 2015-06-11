from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    """Email the subscribers if their locale is current

    This is simply a wrapper for arxiv.tasks.email_subscribers and is
    designed to be called by an external cron job if using Celery is not
    feasible
    """

    def handle(self, *args, **kwargs):
        from arxiv.tasks import email_subscribers
        email_subscribers()

