#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This was my original plan of attack for the assignment. I wanted to assign a
numerical value to each character, so that I could sum the values of the
characters in a word and compare word values to determine anagrams (because
addition doesn't care in what order you add). It would have been unwieldy to
try to assign the character weights to render collisions impossible, but using
Python's built-in hash function is satisfactory in 99.99% of situations. This
uncertainty is why I also supplied solution #2. That being said, I ran a diff
on the results from both algorithms when applied to the input in the kata,
and they're identical.

Note: not all of the inputs are UTF-8 encoded, so I used the 'surrogateescape'
mode to open the files for reading and writing. When the results are written,
non-UTF-8 characters are replaced by a control sequence. The sequences appear
to be unique to the character, so it doesn't affect the processing, just the
presentation of the result.

Created on Mon Oct  5 16:15:03 2020

@author: m
"""
from collections import defaultdict
import os

cwd = os.getcwd()

def hash_string(the_string):
    hash_value = 0
    hash_value = sum([hash_value + hash(each_char) for each_char in the_string])
    return hash_value
    

def run_1(word_list_file):
    word_list = open(word_list_file, "r", errors="surrogateescape").read().splitlines()
    
    anagrams = defaultdict(list)
    
    for word in word_list:
        key = hash_string(word)
        if not key in anagrams.keys():
            anagrams[key] = [word]
        else:
            anagrams[key].append(word)
            
    return anagrams