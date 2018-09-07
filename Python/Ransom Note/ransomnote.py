#!/bin/python3

# Project: Hash Tables: Ransom Note
# This: ransomnote.py
# Author: C Robinson
# Date: 07 Sep 2018
# Purpose: Solve Hash Tables: Ransom Note. What this problem does:
#                 - Uses collection Counter to create a 'hashmap' of each list given.
#                 - Returns true or false (yes or no) if the note minus source list is 0.


import math
import os
import random
import re
import sys
from collections import Counter as c

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    n = c(note)
    m = c(magazine)
    if(len(n - m) == 0):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
