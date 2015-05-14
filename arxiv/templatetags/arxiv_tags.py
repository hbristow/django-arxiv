from django import template
from django.contrib.staticfiles import finders
register = template.Library()

@register.filter
def stringify(iterable):
    """Stringify an iterable of strings"""
    return ', '.join(iterable[:-2]+[' and '.join(iterable[-2:])])

@register.simple_tag
def inline(path):
    """Load the contents of the given static file (for inline CSS/js)"""
    realpath = finders.find(path)
    with open(realpath) as f:
        return f.read()
