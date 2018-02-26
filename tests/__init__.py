# Copyright (c) 2012-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from __future__ import absolute_import

__all__ = ('top_dir', 'test_dir')

import sys, os, importlib
if sys.version_info.major <= 2:
    sys.modules["unittest"] = importlib.import_module("unittest2")
test_dir = os.path.dirname(os.path.abspath(__file__))
top_dir = os.path.dirname(test_dir)
del sys, os, importlib
