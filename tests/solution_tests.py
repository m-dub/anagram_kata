#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:36:14 2020

@author: m
"""

from scripts import solution1, solution2

def test_empty_1():
    assert solution1.run_1("tests/empty_list.txt") == {}
    
def test_empty_2():
    assert solution2.run_2("tests/empty_list.txt") == {}
    
def test_all_unique_1():
    expected = [['cat'], ['dog'], ['bird']]
    assert list(solution1.run_1("tests/all_unique.txt").values()) == expected
    
def test_all_unique_2():
    expected = {'act': ['cat'], 'dgo': ['dog'], 'bdir': ['bird']}
    assert solution2.run_2("tests/all_unique.txt") == expected
    
def test_alpha_pair_1():
    expected = [['goat', 'agot'], ['coat', 'taco']]
    assert list(solution1.run_1("tests/alpha_pair.txt").values()) == expected
    
def test_alpha_pair_2():
    expected = {'agot': ['goat', 'agot'], 'acot': ['coat', 'taco']}
    assert solution2.run_2("tests/alpha_pair.txt") == expected
    
def test_case_sensitive_alpha_pair_1():
    expected = [['Goat', 'aGot'], ['coat'], ['Taco']]
    assert list(solution1.run_1("tests/case_sensitive_alpha_pair.txt").values()) == expected
    
def test_case_sensitive_alpha_pair_2():
    expected = {'Gaot': ['Goat', 'aGot'], 'acot': ['coat'], 'Taco': ['Taco']}
    assert solution2.run_2("tests/case_sensitive_alpha_pair.txt") == expected
    
def test_alpha_triple_1():
    expected = [['lair', 'liar', 'rail']]
    assert list(solution1.run_1("tests/alpha_triple.txt").values()) == expected
    
def test_alpha_triple_2():
    expected = {'ailr': ['lair', 'liar', 'rail']}
    assert solution2.run_2("tests/alpha_triple.txt") == expected

# These next two are testing with a hyphen as the special character, just to see.    
def test_alphaspecial_pair_1():
    expected = [['go-to', 'to-go']]
    assert list(solution1.run_1("tests/alphaspecial.txt").values()) == expected
    
def test_alphaspecial_pair_2():
    expected = {'-goot': ['go-to', 'to-go']}
    assert solution2.run_2("tests/alphaspecial.txt") == expected

# These two are testing alphanumeric inputs even though there are none in the
# input. I still want to illustrate that the solutions would work regardless.
def test_alphanumeric_pair_1():
    expected = [['a006', '600a']]
    assert list(solution1.run_1("tests/alphanumeric.txt").values()) == expected
    
def test_alphanumeric_pair_2():
    expected = {'006a': ['a006', '600a']}
    assert solution2.run_2("tests/alphanumeric.txt") == expected