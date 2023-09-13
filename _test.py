import os
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
from configparser import ConfigParser

from 888888888888 import *


# =====================================================================================================================
class Test__888888888888:
    VICTIM: Type[888888888888] = type("VICTIM", (888888888888,), {})

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        self.VICTIM = type("VICTIM", (888888888888,), {})

    # -----------------------------------------------------------------------------------------------------------------
    def test__ClassMethod_and_obj(self):
        assert self.VICTIM.get(self.888888888888) == self.888888888888


# =====================================================================================================================
