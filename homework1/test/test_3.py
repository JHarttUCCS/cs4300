# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

from ..task3 import *

import pytest


# Test the pos_neg function for all possible outputs
def test_pos_neg():
    assert pos_neg(-300) == -1
    assert pos_neg(0) == 0
    assert pos_neg(42) == 1

# test the primes function using the raw output
def test_primes(capsys):
    print_ten_primes()
    captured = capsys.readouterr()
    assert captured.out == "2, 3, 5, 7, 11, 13, 17, 19, 23, 29\n"

# Test the sum
def test_sum():
    assert sum(1, 100) == 5050
