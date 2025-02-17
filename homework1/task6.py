# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

# import os.path


# Count the words using the split() function
def count_words(filepath):
    with open(filepath, 'r') as f:
        return len(f.read().split())
