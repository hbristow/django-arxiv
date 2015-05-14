Django arXiv
============
A Django app providing a custom [arXiv](http://arxiv.org) email feed to subscribers

Quick Start
-----------

1. Install `django-arxiv` and its dependencies using `pip`:

        pip install git+https://github.com/hbristow/django-arxiv

2. Add `arxiv` and `solo` to your INSTALLED_APPS setting:

        INSTALLED_APPS = (
            ...
            'solo',
            'arxiv',
        )

2. Include the `arxiv` URLconf in your project `urls.py`:

        url(r'^arxiv/', include('arxiv.urls')),

3. Run `python manage.py migrate` to create the `arxiv` models
   and install the initial data fixtures

4. Navigate to `http://.../arxiv/` to subscribe to the feed

5. Start the `celery` service so that emails are sent automatically
   by the server:

        celery -A project-name beat

### Subscribe View
![Subscribe view](docs/subscribe.png)

### Web View of Email Feed
![Feed view](docs/feed.png)
