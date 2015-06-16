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
    try:
        subscriber = models.Subscriber.objects.get(uuid=uuid)
        email = subscriber.email
        message = '{email} was unsubscribed successfully'.format(email=email)
        subscriber.delete()
    except models.Subscriber.DoesNotExist:
        message = 'There are no subscribers with that identifier'
    return render(request, 'arxiv/message.html', {'message': message})


# ----------------------------------------------------------------------------
# Render the latest
# ----------------------------------------------------------------------------
def latest(request):
    """Render the latest submissions in the given subject areas"""
    query = request.GET
    try:
        uuid = query.get('uuid')
        subscriber = models.Subscriber.objects.get(uuid=uuid)
        subjects = subscriber.values_list('subjects__cat', flat=True)
    except models.Subscriber.DoesNotExist:
        subjects = query.get('subjects')
        if subjects:
            subjects = subjects.split(',')
        else:
            subjects = models.Subject.objects.all().values_list('cat', flat=True)

    # render the feed
    return render(request, 'arxiv/email.html', {
        'feed': feed.today(*subjects),
    })
