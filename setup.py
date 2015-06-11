from setuptools import setup, find_packages

# ----------------------------------------------------------------------------
# Arxiv
# ----------------------------------------------------------------------------
setup(
    name='django-arxiv',
    version='0.1',
    description='A Django app providing a custom arXiv feed to subscribers',
    long_description=open('README.md').read(),
    author='Hilton Bristow',
    author_email='hilton.bristow+arxiv@gmail.com',
    url='https://github.com/hbristow/django-arxiv',
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=[
        'django >= 1.7',
        'django-solo',
        'xmltodict',
        'celery',
        'pytz',
        'six',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False)
