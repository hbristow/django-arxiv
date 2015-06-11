from django.core.management.base import BaseCommand, CommandError
from django.template import loader, Context
import os
import re
import subprocess

def read(filename):
    """Read the contents of a file into a string"""
    with open(filename) as f:
        return f.read()

class Command(BaseCommand):
    """Inline the arXiv email template components"""

    def handle(self, *args, **kwargs):
        import arxiv

        # load the template resources
        module = os.path.dirname(os.path.realpath(arxiv.__file__))
        base = read(os.path.join(module, 'templates/arxiv/email.html'))
        feed = read(os.path.join(module, 'templates/arxiv/feed.html'))

        # get the CSS stylesheets to inline
        style = os.path.join(module, 'static/arxiv/css/style.css')
        email = os.path.join(module, 'static/arxiv/css/email.css')

        # sanitize the templates
        feed = re.sub(r'{% load [^%]+ %}', '', feed)
        sep  = base.find('<')
        head, body = base[:sep], base[sep:]

        # perform the template inclusion
        body = re.sub(r'{% include "arxiv/feed.html" %}', feed, body)
        body = re.sub(r'\n\s+\n', '\n\n', body)

        # inline the CSS using Premailer
        premailer = subprocess.Popen(
            [
                'premailer',
                '--mode', 'html',
                '--css', ','.join((style,email)),
                '--remove-classes'
            ],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE)

        with open(os.path.join(module, 'templates/arxiv/email.inlined.html'), 'w') as f:
            body = premailer.communicate(body)[0]
            f.write(head + body)
