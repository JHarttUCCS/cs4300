# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

from ..task_4 import *

import pytest


def test_apply_discount():
    assert apply_discount(10, 0.71) == 7.1
    assert apply_discount(43.32, 0.5) == 21.66
    assert apply_discount(8.67, 1) == 8.67