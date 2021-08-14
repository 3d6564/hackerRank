#!/bin/python3
import math
import os
import random
import re
import sys
import statistics as stats

# Using the Q3 - Q1 method for Interquartile Range.
def interQuartile(values, freqs):
    a = []
    for i in range(0,n):
        for d in range(0,freqs[i]):
            a.append(values[i])
    a.sort()
    m = int(len(a)/2)
    if len(a) % 2 == 0:
        s1 = float(stats.median(a[:m]))
        s2 = float(stats.median(a[m:]))
    else:
        s1 = float(stats.median(a[:m]))
        s2 = float(stats.median(a[m+1:]))        
    print(s2-s1)

# Provided code by HackerRank
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
