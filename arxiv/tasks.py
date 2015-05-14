from __future__ import absolute_import
from django.template.loader import get_template
from django.template import Context
from celery.schedules import crontab
import celery
import collections

from arxiv import feed, models

CELERYBEAT_SCHEDULE = {
    # Executes on weekdays every 30 minutes (timezones are spaced 30 minutes apart)
    'email-subscribers': {
        'task': 'arxiv.tasks.email_subscribers',
        'schedule': crontab(minute='*/1')
    }
}

@celery.task
def email_subscribers():
    """Email subscribers with a daily digest of their subject areas"""
    mail_server = models.MailServer.get_solo()

    # get the timezones which need updating
    timezones = models.Subscriber.objects.values_list('timezone', flat=True).distinct()

    # get all subscribers in the timezones that need notifying
    subscribers = models.Subscriber.objects.filter(timezone__in=timezones).prefetch_related('subjects')

    # store the subscribers against the unique combinations of subjects
    combinations = collections.defaultdict(list)
    for subscriber in subscribers:
        subjects = tuple(sorted(subscriber.subjects.all().values_list('cat', flat=True)))
        combinations[subjects].append(subscriber)

    # fetch all unique combinations of subjects and email the subscribers
    for subjects, subscribers in combinations.iteritems():
        articles = feed.today(*subjects)
        template = get_template('arxiv/email.inlined.html')

        for subscriber in subscribers:
            rendered = template.render(Context({
                'feed': articles,
                'subscriber': subscriber
            }))
            mail_server.send_mail('arXiv Feed', rendered, [subscriber.email])
