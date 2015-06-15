from django.conf.urls import patterns, include, url

urlpatterns = patterns('arxiv.views',
    url(r'^$', 'subscribe', name='index'),
    url(r'^subscribe/$', 'subscribe', name='subscribe'),
    url(r'^unsubscribe/$', 'unsubscribe', name='unsubscribe'),
    url(r'^latest/$', 'latest', name='latest')
)
