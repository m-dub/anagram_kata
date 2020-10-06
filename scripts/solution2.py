#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
As you can tell, this implementation is mostly the same, except that I'm using
the output of sorting each word list element as the key in a dictionary. I
think this is a tiny bit slower because lookups on strings are slower than
lookups on numbers, but in this case it seems to be a negligible difference.

Created on Mon Oct  5 16:15:03 2020

@author: m
"""
from collections import defaultdict
import os

cwd = os.getcwd()

def run_2(word_list_file):
    word_list = open(word_list_file, "r", errors="surrogateescape").read().splitlines()
    
    anagrams = defaultdict(list)
    
    for word in word_list:
        key = ''.join(sorted(word))
        if not key in anagrams.keys():
            anagrams[key] = [word]
        else:
            anagrams[key].append(word)

    return anagrams
