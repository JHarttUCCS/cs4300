# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

from ..task7 import *

import numpy as np
import pytest


# Test np dot product using multiple arrays of different shapes and 
# comparing them to an expected output
def test_np_dot_product():
    matA = np.array([[ 1, 2],
                     [ 3, 4],
                     [ 5, 6],
                     [ 7, 8]])

    matB = np.array([[-8, 6, 7],
                     [ 5,-3, 0]])

    matC = np.array([[-2,-1, 0],
                     [-1, 0, 1],
                     [ 0, 1, 2]])

    finalMat = np.array([[ -4,   5,  14],
                         [  2,  25,  48],
                         [  8,  45,  82],
                         [ 14,  65, 116]])

    assert np.array_equal(np_dot_product(matA, matB, matC), finalMat)
