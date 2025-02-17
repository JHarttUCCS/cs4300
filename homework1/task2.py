# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

# Simple factorial function
def fact(n):
    if n < 2:
        return 1
    
    return fact(n - 1) * n

# Simple square root function
def sqrt(n):
    return n ** 0.5

# Simple string splicing function
def splice(str1, str2, n):
    # Demonstrates string splicing and string addition
    return str1[:n] + str2[n:]

# Simple xnor function
def xnor(b1, b2):
    # Demonstrates boolean algrebra in python
    return not(b1 ^ b2)
