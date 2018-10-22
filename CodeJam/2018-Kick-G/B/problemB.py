import fileinput
import numpy as np
import math

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
    # print ("L",L)
    # print ("R",R)
    # print ("K",K)

    # S = 0
    # for i in range(Q):
    #     L_tmp = L.copy()
    #     R_tmp = R.copy()
    #     for j in range(K[i]):
    #         if (len(L_tmp)>0):
    #             #print ("max",L_tmp,R_tmp)
    #             num = R_tmp.index(max(R_tmp))
    #             score = R_tmp[num]
    #             R_tmp[num] = R_tmp[num]-1
    #             L_tmp,R_tmp = DelS(L_tmp,R_tmp)
    #             #print (L_tmp,R_tmp)
    #             #print (score)
    #         else:
    #             score = 0
    #     S += score*(i+1)
    #print (S)
    
    maxScore = max(R)
    minScore = min(L)

    scoreNum = [0]*(maxScore-minScore+1)
    #listK = []
    
    for i in range(len(L)):
        
        lenTmp = R[i]-L[i]+1
        start = L[i]-minScore
        #print (start)
        for j in range(lenTmp):
            #print (scoreNum)
            #print (j)
            scoreNum[start+j] += 1
            
    #print (scoreNum)

    for i in range(Q):
        #print (K[i],len(scoreNum),maxScore)
        sum = 0
        numMa = len(scoreNum)
        k = 1
        while 1:
            if sum >= K[i]:
                break
            if k > numMa:
                S = 0
                break
            S = maxScore+1-k
            sum += scoreNum[numMa-k]
            k += 1
        

        

    print ("Case #{}: {}".format(case, S))