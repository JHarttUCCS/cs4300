# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

from ..task5 import *

import pytest


# Test the print output of print first 3 books
def test_print_first_3_books(capsys):
    print_first_3_books()
    captured = capsys.readouterr()
    assert captured.out == "Words of Radiance by Brandon Sanderson\nSpice and Wolf Volume 5 by Isuna Hasekura\nDune by Frank Herbert\n"


# test each key-value pair in the students dictionary
def test_students():
    assert students["Hannibal Barca"] == 1234567890
    assert students["Jacob Hartt"] == 7198675309
    assert students["Kraft Lawrence"] == 4242424242
