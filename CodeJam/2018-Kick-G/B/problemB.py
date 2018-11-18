import fileinput
import numpy as np
import math

import sys
 
sys.setrecursionlimit(1000000)

f = fileinput.input()
def input():
    return f.readline()

def DelS(L,R):
    for i in range(len(L)):
        #print (R,L,i)
        if L[i] > R[i]:
            del L[i]
            del R[i]
            return L,R
    return L,R


T = int(input())
for case in range(1, T+1):
    N, Q= [int(x) for x in input().split()]
    data = [[int(x) for x in input().split()] for i in range(3)]
    #print (data)
    X = []
    Y = []
    Z = []
    L = []
    R = []
    K = []
    A = [data[0][2],data[1][2],data[2][2]]
    B = [data[0][3],data[1][3],data[2][3]]
    C = [data[0][4],data[1][4],data[2][4]]
    M = [data[0][5],data[1][5],data[2][5]]

    X += [data[0][0],data[0][1]]
    Y += [data[1][0],data[1][1]]
    Z += [data[2][0],data[2][1]]

    if N >= 3:
        for i in range(2,N):
            X += [(A[0]*X[i-1]+B[0]*X[i-2]+C[0])%M[0]]
            Y += [(A[1]*Y[i-1]+B[1]*Y[i-2]+C[1])%M[1]]
    if Q >= 3:
        for i in range(2,Q):
            Z += [(A[2]*Z[i-1]+B[2]*Z[i-2]+C[2])%M[2]]
    
    for i in range(N):
        L += [min(X[i],Y[i])+1]
        R += [max(X[i],Y[i])+1]
    
    for i in range(Q):
        K += [Z[i]+1]
    
    # print ("X",X)
    # print ("Y",Y)
    # print ("Z",Z)
    #print ("L",L)
    #print ("R",R)
    #print ("K",K)

    #S = 0
    # for i in range(len(K)):
        # L_tmp = [j for j in L]
        # R_tmp = [j for j in R]
        # K_tmp = K[i]
        # def function(L_tmp,R_tmp,K_tmp):
        #     if (not R_tmp):
        #         return 0
        #     if K_tmp == 1:
        #         return max(R_tmp)
        #     else:
        #         R_index = R_tmp.index(max(R_tmp))
        #         if (R_tmp[R_index]-L_tmp[R_index]+1)>int(K_tmp/2):
        #             R_tmp[R_index] -= int(K_tmp/2)
        #             return function(L_tmp,R_tmp,K_tmp-int(K_tmp/2))
        #         else:
        #             len_tmp = R_tmp[R_index]-L_tmp[R_index]+1
        #             R_tmp.pop(R_index)
        #             L_tmp.pop(R_index)
        #             return function(L_tmp,R_tmp,K_tmp-len_tmp)

        # S += function(L_tmp,R_tmp,K_tmp)*(i+1)

    def find_x(x):
        sum_data = 0
        for i in range(len(R)):
            big = R[i]
            small = L[i]
            if x>big:
                sum_data += 0
            elif x>small:
                sum_data += big-x+1
            else:
                sum_data += big-small+1
        return sum_data

    S = 0
    max_score = max(R)
    min_score = min(L)
    for i in range(len(K)):
        right = max_score
        left = min_score
        mid = int(max_score+min_score)/2
        while (right>left+1):
            tmp = find_x(mid)
            #print ('find_x',tmp,'mid',mid,'left',left,'right',right)
            if tmp >= K[i]:
                left = mid
                mid = int((right+left)/2)
            else:
                right = mid
                mid = int((right+left)/2)
        if find_x(left) >= K[i]:
            S += left*(i+1)

        
    print ("Case #{}: {}".format(case, S))