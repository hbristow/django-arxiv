from django.conf.urls import patterns, include, url

urlpatterns = patterns('arxiv.views',
    url(r'^$', 'subscribe'),
    url(r'^subscribe/$', 'subscribe'),
    url(r'^unsubscribe/$', 'unsubscribe'),
    url(r'^latest/$', 'latest')
)
