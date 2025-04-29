annotate
========

Function annotations.

Overview
========

**@annotate**

| Decorator to set a function's __annotations__ like Py3.
| https://www.python.org/dev/peps/pep-3107/

`PyPI record`_.

`Documentation`_.

Examples
--------

.. code:: python

  from typing   import Optional, Tuple, Union, Sequence
  from annotate import annotate

  from .lib import cached
  from .    import jni

  from .jobjectbase import JObjectBase
  from .jclass      import JClass
  from .jobject     import JObject


  class JArray(JObjectBase):
      """Java Array"""

      @classmethod
      @annotate('JArray', size=Union[int, long])
      def newBooleanArray(cls, size):
          ...
      ...
      @classmethod
      @annotate('JArray', size=Union[int, long])
      def newDoubleArray(cls, size):
          ...
      @classmethod
      @annotate('JArray', size=Union[int, long])
      def newStringArray(cls, size):
          ...
      @classmethod
      @annotate('JArray', size=Union[int, long], component_class=JClass)
      def newObjectArray(cls, size, component_class):
          ...

      @annotate(jenv=jni.JNIEnv, jarr=jni.jarray, borrowed=bool)
      def __init__(self, jenv, jarr, borrowed=False):
          ...

      def __hash__(self):
          return super(JArray, self).__hash__()

      def __len__(self):
          return self.getLength()

      @annotate(JObject, borrowed=bool)
      def asObject(self, borrowed=False):
          ...

      @cached
      @annotate(int)
      def getLength(self):
          ...

      @annotate(bool, idx=int)
      def getBoolean(self, idx):
          ...
      ...
      @annotate(float, idx=int)
      def getDouble(self, idx):
          ...
      @annotate(Optional[str], idx=int)
      def getString(self, idx):
          ...
      @annotate(Optional[JObject], idx=int)
      def getObject(self, idx):
          ...

      @annotate(idx=int, val=bool)
      def setBoolean(self, idx, val):
          ...
      @annotate(idx=int, val=str)
      def setChar(self, idx, val):
          ...
      ...
      @annotate(idx=int, val=Union[int, long])
      def setLong(self, idx, val):
          ...
      @annotate(idx=int, val=float)
      def setDouble(self, idx, val):
          ...
      @annotate(idx=int, val=Optional[str])
      def setString(self, idx, val):
          ...
      @annotate(idx=int, val=Optional[JObject])
      def setObject(self, idx, val):
          ...

      @annotate('JArray', start=int, stop=int, step=int)
      def getBooleanSlice(self, start, stop, step):
          ...
      ...
      @annotate('JArray', start=int, stop=int, step=int)
      def getDoubleSlice(self, start, stop, step):
          ...
      @annotate('JArray', start=int, stop=int, step=int)
      def getStringSlice(self, start, stop, step):
          ...
      @annotate('JArray', start=int, stop=int, step=int)
      def getObjectSlice(self, start, stop, step):
          ...

      @annotate(start=int, stop=int, step=int, val=Sequence[bool])
      def setBooleanSlice(self, start, stop, step, val):
          ...
      @annotate(start=int, stop=int, step=int, val=Union[Sequence[str], str])
      def setCharSlice(self, start, stop, step, val):
          ...
      @annotate(start=int, stop=int, step=int,
                val=Union[Sequence[Union[int,bytes]], (bytes, bytearray)])
      def setByteSlice(self, start, stop, step, val):
          ...
      ...
      @annotate(start=int, stop=int, step=int, val=Sequence[float])
      def setDoubleSlice(self, start, stop, step, val):
          ...
      @annotate(start=int, stop=int, step=int, val=Sequence[Optional[str]])
      def setStringSlice(self, start, stop, step, val):
          ...
      @annotate(start=int, stop=int, step=int, val=Sequence[Optional[JObject]])
      def setObjectSlice(self, start, stop, step, val):
          ...

      @annotate(Tuple)
      def getBooleanBuffer(self):
          with self.jvm as (jvm, jenv):
              is_copy = jni.jboolean()
              return jenv.GetBooleanArrayElements(self._jobj, is_copy), jni.sizeof(jni.jboolean), b"B", is_copy
      ...
      @annotate(Tuple)
      def getDoubleBuffer(self):
          with self.jvm as (jvm, jenv):
              is_copy = jni.jboolean()
              return jenv.GetDoubleArrayElements(self._jobj, is_copy), jni.sizeof(jni.jdouble), b"d", is_copy

      @annotate(buf=object)
      def releaseBooleanBuffer(self, buf):
          with self.jvm as (jvm, jenv):
              jenv.ReleaseBooleanArrayElements(self._jobj, jni.cast(buf, jni.POINTER(jni.jboolean)))
      ...
      @annotate(buf=object)
      def releaseDoubleBuffer(self, buf):
          with self.jvm as (jvm, jenv):
              jenv.ReleaseDoubleArrayElements(self._jobj, jni.cast(buf, jni.POINTER(jni.jdouble)))

Installation
============

Prerequisites:

+ Python 3.10 or higher

  * https://www.python.org/

+ pip and setuptools

  * https://pypi.org/project/pip/
  * https://pypi.org/project/setuptools/

To install run:

  .. parsed-literal::

    python -m pip install --upgrade |package|

Development
===========

Prerequisites:

+ Development is strictly based on *tox*. To install it run::

    python -m pip install --upgrade tox

Visit `Development page`_.

Installation from sources:

clone the sources:

  .. parsed-literal::

    git clone |respository| |package|

and run:

  .. parsed-literal::

    python -m pip install ./|package|

or on development mode:

  .. parsed-literal::

    python -m pip install --editable ./|package|

License
=======

  | |copyright|
  | Licensed under the zlib/libpng License
  | https://opensource.org/license/zlib
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Adam Karpierz <adam@karpierz.net>

.. |package| replace:: annotate
.. |package_bold| replace:: **annotate**
.. |copyright| replace:: Copyright (c) 2012-2025 Adam Karpierz
.. |respository| replace:: https://github.com/karpierz/annotate.git
.. _Development page: https://github.com/karpierz/annotate
.. _PyPI record: https://pypi.org/project/annotate/
.. _Documentation: https://annotate.readthedocs.io/
