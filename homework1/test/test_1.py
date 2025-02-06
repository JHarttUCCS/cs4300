# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

from ..task_1 import *

import pytest


def test_1(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
