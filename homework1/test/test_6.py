# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025

from ..task6 import *

import os
import pytest

testDir = os.path.join('..', 'res')


def run_test_word_count(filepath):
    with open(filepath, 'r') as f:
        words = len(f.read().split())
        assert count_words(filepath) == words

# print(testDir)


# Dynamically register the test functions in the globals() namespace for pytest to find
# inspired by but not copied from a ChatGPT response: https://chatgpt.com/share/67b28092-c43c-8006-a8ac-f5200ad55613
for fileName in os.listdir(testDir):
    if fileName.endswith('.txt'):
        testName = f"test_count_words_{os.path.splitext(fileName)[0]}"
        filepath = os.path.join(testDir, fileName)

        # Declare a temporary function and add it to the globals space
        def tmp_func():
            run_test_word_count(filepath)

        globals()[testName] = tmp_func
