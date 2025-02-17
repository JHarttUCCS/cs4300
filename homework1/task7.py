# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

import numpy as np


# Calculate the dot product chain of 3 seperate matrices
def np_dot_product(matA, matB, matC):
    return np.dot(np.dot(matA, matB), matC)
