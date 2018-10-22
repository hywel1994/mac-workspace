import fileinput
import numpy as np
import math

import sys
 
sys.setrecursionlimit(1000000)

global N,M,E,SR,SC,TR,TC,data,ans



f = fileinput.input()
def input():
    return f.readline()

def score(X,Y):
    global N,M,E,SR,SC,TR,TC,data,ans
    if (ans[X][Y]>=-1):
        return ans[X][Y]
    tmpScore = []
    #print (X,Y)
    ans[X][Y] = 0
    print (ans)
    if X+1 < N :
        if data[X+1][Y] > -100000:
            tmpScore += [score(X+1,Y)+data[X+1][Y]]
    if X-1 >= 0 :
        if data[X-1][Y] > -100000:
            tmpScore += [score(X-1,Y)+data[X-1][Y]]
    if Y+1 < M:
        if data[X][Y+1] > -100000:
            tmpScore += [score(X,Y+1)+data[X][Y+1]]
    if Y-1 >= 0 :
        if data[X][Y-1] > -100000:
            tmpScore += [score(X,Y-1)+data[X][Y-1]]
    #print (tmpScore)

    if len(tmpScore) <= 0:
        ans[X][Y] = -1
        return -1
    if max(tmpScore) < 0:
        ans[X][Y] = -1
        return -1
    else:
        ans[X][Y] = max(tmpScore)
        return ans[X][Y]

def score2(X,Y):
    global N,M,E,SR,SC,TR,TC,data,ans
    if (ans[X][Y]>=-1):
        return ans[X][Y]
    tmpScore = []


T = int(input())
for case in range(1, T+1):
    N,M,E,SR,SC,TR,TC = [int(x) for x in input().split()]
    data = [[int(x) for x in input().split()] for i in range(N)]
    ans = [([-100000] * M) for i in range(N)]
    ans[SR-1][SC-1] = E
    S = score(TR-1,TC-1)
    
    

    print ("Case #{}: {}".format(case, S))