from typing import *
import pytest

import pathlib
import shutil
from tempfile import TemporaryDirectory
from configparser import ConfigParser
from pytest import mark


# =====================================================================================================================
# KEEP FILES IN ROOT! OR IMPORT PRJ_MODULE WOULD FROM SYSTEM! NOT THIS SOURCE!!!
from PRJ_NEW__ import *


# =====================================================================================================================
def func_example(arg1: Any, arg2: Any) -> str:
    return f"{arg1}{arg2}"


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="p1,p2,_EXPECTED,_MARK",
    argvalues=[
        # TRIVIAL -------------
        (1, None, "1None", None),
        (1, 2, "12", None),

        # LIST -----------------
        (1, [], "1[]", None),

        # MARKS -----------------
        (1, 2, None, mark.skip),
        (1, 2, None, mark.skipif(True)),
        (1, 2, None, mark.skipif(False)),
        (1, 2, None, mark.xfail),
        (1, 2, "12", mark.xfail),
    ]
)
def test__func_ONE(p1, p2, _EXPECTED, _MARK):
    func_link = func_example
    try:
        value_actual = func_link(arg1=p1, arg2=p2)
    except Exception as exx:
        value_actual = exx

    # MARKS -------------------------
    print(f"{mark.skipif(True)=}")
    if _MARK == mark.skip:
        pytest.skip()
    elif isinstance(_MARK, pytest.MarkDecorator) and _MARK.name == "skipif" and all(_MARK.args):
        pytest.skip()
    elif _MARK == mark.xfail:
        assert value_actual != _EXPECTED
    else:
        assert value_actual == _EXPECTED


# =====================================================================================================================
def _FUNC_UNIVERSAL(func_link, args, kwargs, _EXPECTED, _MARK):
    args = args or ()
    kwargs = kwargs or {}

    try:
        actual_value = func_link(*args, **kwargs)
    except Exception as exx:
        actual_value = exx

    # MARKS -------------------------
    print(f"{mark.skipif(True)=}")
    if _MARK == mark.skip:
        pytest.skip("skip")
    elif isinstance(_MARK, pytest.MarkDecorator) and _MARK.name == "skipif" and all(_MARK.args):
        pytest.skip("skipIF")

    if _MARK == mark.xfail:
        if isinstance(_EXPECTED, Exception):
            assert not isinstance(actual_value, _EXPECTED), "xfail"
        else:
            assert actual_value != _EXPECTED, "xfail"
    else:


        if isinstance(_EXPECTED, Exception):
            assert isinstance(actual_value, _EXPECTED)
        else:
            assert actual_value == _EXPECTED


# =====================================================================================================================
@pytest.mark.parametrize(argnames="func_link", argvalues=[func_example, ])
@pytest.mark.parametrize(
    argnames="args, kwargs, _EXPECTED, _MARK",
    argvalues=[
        # TRIVIAL -------------
        ((1, None), {}, "1None", None),
        ((1, 2), {}, "12", None),

        # LIST -----------------
        ((1, []), {}, "1[]", None),

        # MARKS -----------------
        ((1, 2), {}, None, mark.skip),
        ((1, 2), {}, None, mark.skipif(True)),
        ((1, 2), {}, None, mark.skipif(False)),
        ((1, 2), {}, None, mark.xfail),
        ((1, 2), {}, "12", mark.xfail),
    ]
)
def test__1(func_link, args, kwargs, _EXPECTED, _MARK):
    _FUNC_UNIVERSAL(func_link, args, kwargs, _EXPECTED, _MARK)


# =====================================================================================================================
@pytest.mark.parametrize(argnames="func_link", argvalues=[int, ])
@pytest.mark.parametrize(
    argnames="args, kwargs, _EXPECTED, _MARK",
    argvalues=[
        # (("1", ), {}, 1, None),
        (("hello", ), {}, Exception, None),
    ]
)
def test__1(func_link, args, kwargs, _EXPECTED, _MARK):
    _FUNC_UNIVERSAL(func_link, args, kwargs, _EXPECTED, _MARK)


# =====================================================================================================================
