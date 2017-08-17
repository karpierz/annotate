# coding: utf-8

def annotate(*args, **kargs):

    """Decorator to set a function's __annotations__ like Py3"""

    def decorate(func):
        if not getattr(func, "__annotations__", None):
            func.__annotations__ = kargs.copy()
            if args:
                func.__annotations__["return"] = args[0]
        return func

    return decorate

# eof
