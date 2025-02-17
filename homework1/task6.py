# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

# import os.path


def count_words(filepath):
    f = open(filepath, 'r')

    return len(f.read().split())
