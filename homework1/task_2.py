# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

def fact(n):
    if n < 2:
        return 1
    
    return fact(n - 1) * n

def sqrt(n):
    return n ** 0.5

def splice(str1, str2, n):
    return str1[:n] + str2[n:]

def xnor(b1, b2):
    return not(b1 ^ b2)
