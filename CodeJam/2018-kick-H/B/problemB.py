import fileinput
import numpy as np
import math
import bisect

f = fileinput.input()
def input():
    return f.readline()

T = int(input())
for case in range(1, T+1):
    N= int(input())
    data = str(input())
    #print (data)
    if N%2 == 0:
        num = int(N/2)
    else:
        num = int((N+1)/2)
    max_sum = 0
    for i in range(num):
        max_sum += int(data[i])

    side_tmp = max_sum
    for i in range(0,N-num):
        side_tmp = side_tmp -int(data[i])+int(data[i+num])
        if side_tmp > max_sum:
            max_sum = side_tmp
    
    print ("Case #{}: {}".format(case, int(max_sum)))