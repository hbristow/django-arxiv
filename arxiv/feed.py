from six.moves import urllib
from datetime import datetime, timedelta
import xmltodict

ARXIV_API     = 'http://export.arxiv.org/api/'
ARXIV_QUERY   = 'query?search_query=%28{subjects}%29+AND+submittedDate:[{begin_date}+TO+{end_date}]&start=0&max_results=100'
ARXIV_OR      = '+OR+'
ARXIV_SUBJECT = 'cat:{}'

def request(begin_date, end_date, *subjects):
    """Build a resource request string from the given subjects and date range

    Args:
        begin_date: The start window as a datetime object
        end_date: The end window as a datetime object
        *subjects: The arXiv subjects (eg 'cs.CV')
    """
    begin_date = begin_date.strftime('%Y%m%d%H%M%S')
    end_date = end_date.strftime('%Y%m%d%H%M%S')
    subjects = ARXIV_OR.join(ARXIV_SUBJECT.format(subject) for subject in subjects)

    # build the query
    return ARXIV_API+ARXIV_QUERY.format(subjects=subjects, begin_date=begin_date, end_date=end_date)

def fetch(request):
    """Fetch the given request and return a dictionary"""
    raw  = urllib.request.urlopen(request)
    feed = xmltodict.parse(raw)['feed']
    entries = feed.get('entry', [])
    return entries if isinstance(entries, list) else [entries]

def sanitize(entry):
    """Sanitize an arxiv entry for templating"""
    def listify(item): return item if isinstance(item, list) else [item]
    return {
        'title': entry['title'],
        'authors': [author['name'] for author in listify(entry['author'])],
        'abstract': entry['summary'],
        'published': entry['published'],
        'updated': entry['updated'],
        'url': entry['id'],
        'pdf': entry['link'][1]['@href'],
        'categories': [cat['@term'] for cat in listify(entry['category'])],
        'comment': entry['arxiv:comment']['#text'] if 'arxiv:comment' in entry else ''
    }

def today(*subjects):
    """Return a feed from the last 24 hours for the given subjects

    Args:
        *subjects: The arXiv subjects (eg 'cs.CV')
    """
    end_date = datetime.today()
    begin_date = end_date - timedelta(days=3)
    feed = fetch(request(begin_date, end_date, *subjects))
    feed = [sanitize(entry) for entry in fetch(request(begin_date, end_date, *subjects))]
    return sorted(feed, key=lambda entry: entry['published'], reverse=True)
