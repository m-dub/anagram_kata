#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Here's the file that orchestrates the solution scripts. It sets the CLI
argument parser and prints the results to the respective output files.

Created on Mon Oct  5 22:36:14 2020

@author: m
"""

from . import solution1, solution2
import argparse
import os

cwd = os.getcwd()
default_infile = cwd + "/wordlist.txt"

# set up command-line argument parsing
parser = argparse.ArgumentParser(description='Creates one or two files containing all the anagrams in the input.')
parser.add_argument('-m', '--method', type=int, default=3, help='1 or 2 to pick a solution; 3 for both')
parser.add_argument('-i', '--infile', type=str, default=default_infile, help='file to check for anagrams')

def main():
    arguments = parser.parse_args()
    
    if not arguments.method == 2:
        anagrams1 = solution1.run_1(arguments.infile)
            
        results = open(cwd + "/anagrams1.txt", "w", encoding="utf-8", errors="surrogateescape")
        for key in anagrams1.keys():
            results.write(str(anagrams1[key]))
            results.write("\n")
            
    if not arguments.method == 1:
        anagrams2 = solution2.run_2(arguments.infile)
            
        results = open(cwd + "/anagrams2.txt", "w", encoding="utf-8", errors="surrogateescape")
        for key in anagrams2.keys():
            results.write(str(anagrams2[key]))
            results.write("\n")
        
if __name__ == "__main__":
    main()