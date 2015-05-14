from setuptools import setup

# ----------------------------------------------------------------------------
# Arxiv
# ----------------------------------------------------------------------------
setup(
    name = 'django-arxiv',
    version = '0.1',
    description = 'A Django app providing a custom arXiv feed to subscribers',
    long_description = open('README.md').read(),
    author = 'Hilton Bristow',
    author_email = 'hilton.bristow+arxiv@gmail.com',
    url = 'https://github.com/hbristow/django-arxiv',
    packages = [
        'arxiv'
    ],
    setup_requires = [
        'django >= 1.7',
        'django-solo',
        'celery'
    ],
    zip_safe = False)
