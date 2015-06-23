from __future__ import absolute_import
from django.template.loader import get_template
from django.template import Context
from celery.schedules import crontab
import celery
import collections

from arxiv import feed, models, time

CELERYBEAT_SCHEDULE = {
    # Executes on weekdays every 15 minutes (timezones are spaced 15 minutes apart)
    'email-subscribers': {
        'task': 'arxiv.tasks.email_subscribers',
        'schedule': crontab(minute='*/15')
    }
}


@celery.task
def email_subscribers():
    """Email subscribers with a daily digest of their subject areas"""

    # get the timezones which need updating
    timezones = models.Subscriber.objects.values_list('timezone', flat=True).distinct()
    timezones = [zone for zone in timezones if time.satisfies(time.now(zone),
        weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        hour = [07],
        minute = [0]
    )]

    # get all subscribers in the timezones that need notifying
    subscribers = models.Subscriber.objects.filter(timezone__in=timezones).prefetch_related('subjects')

    # notify those subscribers
    for subscriber in subscribers:
        email_feed(subscriber)


@celery.task
def email_feed(subscriber):
    """Email a recipient with the given subjects"""
    mail_server = models.MailServer.get_solo()

    subjects = subscriber.subjects.all().values_list('cat', flat=True)
    articles = feed.today(*subjects)
    template = get_template('arxiv/email.inlined.html')
    rendered = template.render(Context({
        'feed': articles,
        'subscriber': subscriber,
        'domain': mail_server.domain,
    }))

    mail_server.send_mail('arXiv Feed', rendered, [subscriber.email])
