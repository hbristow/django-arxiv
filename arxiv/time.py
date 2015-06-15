from datetime import datetime, timedelta
import itertools
import pytz

def now(timezone):
    """Get the current time in the given timezone

    Args:
        timezone: The desired timezone as a string. eg 'US/Eastern'
    """
    utc = pytz.timezone('UTC').localize(datetime.utcnow())
    return utc.astimezone(pytz.timezone(timezone))


def satisfies(query, **kwargs):
    """Check whether a given datetime object satisfies day and time predicates

    Keyword Args:
        month: The month predicate (January, February, ...)
        day: The day of month predicate [1 31)
        weekday: The day of week predicate (Sunday, Monday, ...)
        hour: The hour of day predicate [0 24)
        minute: The minute of hour predicate [0 60)
    """
    formatters = {
        'month': lambda: datetime.strftime(query, '%B'),
        'weekday': lambda: datetime.strftime(query, '%A'),
        'day': lambda: query.day,
        'hour': lambda: query.hour,
        'minute': lambda: query.minute
    }

    attributes = kwargs.keys()
    predicates = itertools.product(*kwargs.values())

    for values in predicates:
        if all([formatters[attr]() == value for attr,value in zip(attributes,values)]):
            return True
    return False
