# Copyright (c) 2012 Adam Karpierz
# SPDX-License-Identifier: Zlib

from typing import TypeAlias, Any
from collections.abc import Callable

__all__ = ('annotate',)

AnyCallable: TypeAlias = Callable[..., Any]


def annotate(*args: Any, **kwargs: Any) -> Callable[[AnyCallable], AnyCallable]:
    """Decorator to set a function's __annotations__ like Py3."""

    def decorate(func: AnyCallable) -> AnyCallable:
        if not getattr(func, "__annotations__", None):  # pragma: no cover
            func.__annotations__ = kwargs.copy()
            if args:
                func.__annotations__["return"] = args[0]
        return func

    return decorate
