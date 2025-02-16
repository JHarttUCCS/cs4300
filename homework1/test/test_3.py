# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

from ..task_2 import *

import pytest


def test_xnor():
    assert xnor(False, False) == True
    assert xnor(True, False) == False
    assert xnor(False, True) == False
    assert xnor(True, True) == True
