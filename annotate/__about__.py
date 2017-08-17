# coding: utf-8

__all__ = ('__title__', '__summary__', '__uri__', '__version_info__',
           '__version__', '__author__', '__email__', '__copyright__',
           '__license__')

__title__        = "annotate"
__summary__      = "Decorator to set a function's __annotations__ like Py3"
__uri__          = "http://pypi.python.org/pypi/annotate/"
__version_info__ = type("version_info", (), dict(serial=0,
                        major=0, minor=7, micro=4, releaselevel="beta"))
__version__      = "{0.major}.{0.minor}.{0.micro}".format(__version_info__)
__author__       = "Adam Karpierz"
__email__        = "python@python.pl"
__copyright__    = "Copyright (c) 2012-2017 {0}".format(__author__)
__license__      = "zlib/libpng License ; http://opensource.org/licenses/zlib"

# eof
