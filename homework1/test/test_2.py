# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

from ..task_2 import *

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
