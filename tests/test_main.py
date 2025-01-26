# Copyright (c) 2012 Adam Karpierz
# SPDX-License-Identifier: Zlib

import unittest
from typing import Optional, Union

import annotate
from annotate import annotate


class JArray:
    """Java Array"""

    @classmethod
    @annotate('JArray', size=int)
    def newBooleanArray(cls, size):
        ...

    @annotate(borrowed=bool)
    def __init__(self, borrowed=False):
        ...

    @annotate(int)
    def getLength(self):
        ...

    @annotate(bool, idx=int)
    def getBoolean(self, idx):
        ...

    @annotate(int, idx=int)
    def getInt(self, idx, val):
        ...

    @annotate(float, idx=int)
    def getDouble(self, idx):
        ...

    @annotate(Optional[str], idx=int)
    def getString(self, idx):
        ...

    @annotate(idx=int, val=bool)
    def setBoolean(self, idx, val):
        ...

    @annotate(idx=int, val=int)
    def setInt(self, idx, val):
        ...

    @annotate(idx=int, val=float)
    def setDouble(self, idx, val):
        ...

    @annotate(idx=int, val=Optional[str])
    def setString(self, idx, val):
        ...


class MainTestCase(unittest.TestCase):

    def test_main(self):
        self.assertEqual(JArray.newBooleanArray.__annotations__, {"size": int, "return": "JArray"})
        self.assertEqual(JArray.__init__.__annotations__,        {"borrowed": bool})
        self.assertEqual(JArray.getLength.__annotations__,       {"return": int})
        self.assertEqual(JArray.getBoolean.__annotations__,      {"idx": int, "return": bool})
        self.assertEqual(JArray.getInt.__annotations__,          {"idx": int, "return": int})
        self.assertEqual(JArray.getDouble.__annotations__,       {"idx": int, "return": float})
        self.assertEqual(JArray.getString.__annotations__,       {"idx": int, "return": Optional[str]})
        self.assertEqual(JArray.setBoolean.__annotations__,      {"idx": int, "val": bool})
        self.assertEqual(JArray.setInt.__annotations__,          {"idx": int, "val": int})
        self.assertEqual(JArray.setDouble.__annotations__,       {"idx": int, "val": float})
        self.assertEqual(JArray.setString.__annotations__,       {"idx": int, "val": Optional[str]})
