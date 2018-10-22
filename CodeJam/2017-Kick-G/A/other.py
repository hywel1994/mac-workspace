import fileinput
import numpy as np
import math
import sys

def power(x, y, m):
    ret, mul = 1, x % m
    while y:
        if y & 1:
            ret = ret * mul % m
        mul = mul * mul % m
        y >>= 1
    return ret

def solve(A, N, P):
    for i in range(N, 0, -1):
        A = power(A, i, P)
    return A

with open('A-large-practice.in', 'r') as f:
    with open('A-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in range(t):
            arr = [int(x) for x in f.readline().strip().split()]
            A, N, P = arr
            f_out.write('Case #%d: %d\n' % (cas+1, solve(A, N, P)))