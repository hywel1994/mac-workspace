import fileinput
import numpy as np
import math

f = fileinput.input()
def input():
    return f.readline()

T = int(input())
for case in range(1, T+1):
    D, N= [int(x) for x in input().split()]
    data = [[int(x) for x in input().split()] for i in range(N)]
    #print (data)
    time = [0]*N
    maxTime = 0
    for i in range(N):
        time[i] = float(D-data[i][0])/data[i][1]
        maxTime = max(time[i],maxTime)
    v = float(D)/maxTime
    print ("Case #{}: {}".format(case, v))