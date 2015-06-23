import functools
import collections

# ----------------------------------------------------------------------------
# Memoization/Caching
# ----------------------------------------------------------------------------
class cached(object):
    """Last 100 value memoization for functions of any arguments"""

    def __init__(self, func):
        """Cache the function/method of any arguments"""
        self.func = func
        self.cache = collections.OrderedDict()

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # not hashable
            return self.func(*args)
        elif args in self.cache:
            # cached
            return self.cache[args]
        else:
            # new
            value = self.func(*args)
            self.cache[args] = value
            # TODO: Make the number of stored evaluations a variable
            if len(self.cache) > 100:
                self.cache.popitem(last=False)
            return value

    def __repr__(self):
        """Return the original function's docstring"""
        return self.func.__doc__

    def __get__(self, obj, cls):
        """Support instance methods"""
        return functools.partial(self.__call__, obj)
