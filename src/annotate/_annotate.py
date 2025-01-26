# Copyright (c) 2012 Adam Karpierz
# SPDX-License-Identifier: Zlib

__all__ = ('annotate',)


def annotate(*args, **kwargs):
    """Decorator to set a function's __annotations__ like Py3."""

    def decorate(func):
        if not getattr(func, "__annotations__", None):  # pragma: no cover
            func.__annotations__ = kwargs.copy()
            if args:
                func.__annotations__["return"] = args[0]
        return func

    return decorate
