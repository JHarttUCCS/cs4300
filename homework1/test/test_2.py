# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

from ..task2 import *

import pytest


def test_fact():
    assert fact(-1) == 1
    assert fact(6) == 720
    assert fact(1) == 1
    assert fact(2) == 2

def test_sqrt():
    assert sqrt(4.0) == pytest.approx(2.0)
    assert sqrt(2.0) == pytest.approx(1.41421356)
    assert sqrt(2.25) == pytest.approx(1.5)

def test_splice():
    assert splice("CATNIP", "ketchup", 3) == "CATchup"
    assert splice("nothing", "this", 10) == "nothing"
    assert splice("Lady of Venice", "Duck with the spinning head", 5) == "Lady with the spinning head"

def test_xnor():
    assert xnor(False, False) == True
    assert xnor(True, False) == False
    assert xnor(False, True) == False
    assert xnor(True, True) == True
