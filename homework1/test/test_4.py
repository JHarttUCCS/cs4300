# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

from ..task4 import *

import pytest


# Apply discounts using floats and integers in both fields
def test_apply_discount():
    assert apply_discount(10, 0.71) == pytest.approx(2.9)
    assert apply_discount(43.32, 0.5) == pytest.approx(21.66)
    assert apply_discount(8.67, 0) == pytest.approx(8.67)