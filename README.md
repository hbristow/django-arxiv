Django arXiv
============
A Django app providing a custom [arXiv](http://arxiv.org) email feed to subscribers

Quick Start
-----------

1. Install `django-arxiv` and its dependencies using `pip`:

    ```bash
    pip install git+https://github.com/hbristow/django-arxiv
    ```

2. Add `arxiv` and `solo` to your `INSTALLED_APPS` setting:

    ```python
    INSTALLED_APPS = (
        ...
        'solo',
        'arxiv',
    )
    ```

2. Include the `arxiv` URLconf in your project `urls.py`:

    ```python
    url(r'^arxiv/', include('arxiv.urls')),
    ```

3. Run `python manage.py migrate` to create the `arxiv` models
   and install the initial data fixtures

4. Navigate to `http://.../arxiv/` to subscribe to the feed

5. Start the `celery` service so that emails are sent automatically
   by the server:

    ```bash
    celery -A project-name beat
    ```

   Celery may ask you about setting up a task queue broker. See the
   [Celery documentation](http://docs.celeryproject.org/en/latest/getting-started/brokers/)
   for which broker will best suit your needs.

### Subscribe View
![Subscribe view](docs/subscribe.png)

### Web View of Email Feed
![Feed view](docs/feed.png)
