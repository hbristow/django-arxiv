from django.shortcuts import render
from datetime import datetime
import pytz
from arxiv import feed, forms, models

# ----------------------------------------------------------------------------
# (Un-)subscribe
# ----------------------------------------------------------------------------
def subscribe(request):
    """Handle the subscription of new users"""
    if request.method == 'POST':
        # a filled-in form has been received
        model = forms.SubscribeForm(request.POST)
        model.save()
        return render(request, 'arxiv/message.html', {
            'message': 'Thanks, your subscription has been received!'})
    # create a new form
    form = forms.SubscribeForm()
    return render(request, 'arxiv/subscribe.html', {'form': form})

def unsubscribe(request):
    """Unsubscribe the user from the service"""
    uuid = request.GET.get('uuid', '')
    subscriber = models.Subscriber.objects.filter(uuid=uuid)
    if subscriber:
        email = subscriber[0].email
        message = '{email} was unsubscribed successfully'.format(email=email)
        subscriber[0].delete()
    else:
        message = 'There are no subscribers with that identifier'
    return render(request, 'arxiv/message.html', {'message': message})


# ----------------------------------------------------------------------------
# Render the latest
# ----------------------------------------------------------------------------
def latest(request):
    """Render the latest submissions in the given subject areas"""
    query = request.GET
    subjects = query.get('subjects')
    try:
        uuid = query['uuid']
        subscriber = models.Subscriber.objects.get(uuid=uuid)
    except:
        subscriber = None

    # determine the subjects for the query
    if subjects:
        subjects = subjects.split(',')
    elif subscriber:
        subjects = subscriber.values_list('subjects__cat', flat=True)
    else:
        subjects = models.Subject.objects.all().values_list('cat', flat=True)

    # render the feed
    return render(request, 'arxiv/email.html', {
        'feed': feed.today(*subjects),
        'subscriber': subscriber
    })
