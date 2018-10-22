import fileinput
import numpy as np
import math

f = fileinput.input()
def input():
    return f.readline()

T = int(input())
for case in range(1, T+1):
    N, P= [int(x) for x in input().split()]
    R = [int(x) for x in input().split()]
    assert len(R) == N
    Q = [[int(x) for x in input().split()] for i in range(N)]
    
    data = np.zeros((N,P))
    for i in range(N):
        Q[i].sort()
        for j in range(P):
            tmp = float(Q[i][j])/R[i]
            # tmp1 = round(tmp)
            # if tmp >= tmp1*0.9 and tmp <= tmp1*1.1:
            #     data[i,j] = tmp1
            # else:
            #     data[i,j] = 0
            data[i,j] = tmp
    print (data)

    minQ = math.floor(np.min(data)/1.1)
    maxQ = math.ceil(np.max(data)/0.9)

    # for target in range(minQ,maxQ+1):
    #     for i in range(N):
    #         for j in range(P):
    
    #print ("Case #{}: {}".format(case, data))