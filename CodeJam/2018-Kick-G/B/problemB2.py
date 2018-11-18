import fileinput
import numpy as np
import math
import bisect


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
    
    mymap = {}
    student_num = 0
    for i in range(N):
        if L[i] in mymap.keys():
            mymap[L[i]] += 1
        else:
            mymap[L[i]] = 1
        if (R[i]+1) in mymap.keys():
            mymap[(R[i]+1)] -= 1
        else:
            mymap[(R[i]+1)] = -1
        student_num += R[i]-L[i]+1
    
    

    len_my_map = len(mymap)
    mymap = [(k,mymap[k]) for k in sorted(mymap.keys())] 
    # print (mymap)
    bit_arr = [0]*(len_my_map)
    sum_arr = [0]*(len_my_map)
    key_arr = [0]*(len_my_map)
    offset_bit = 0
    sum1 = 0
    for i in range(len_my_map):
        offset_bit += mymap[i][1]
        key_arr[i] = mymap[i][0]
        bit_arr[i] = offset_bit
        if i+1 < len_my_map:
            sum1 += offset_bit*(mymap[i+1][0]-key_arr[i])
            sum_arr[i+1] = sum1
    # print ('key_arr',key_arr)
    # print ('bit_arr',bit_arr)
    # print ('sum_arr',sum_arr)

    S = 0
    # print (student_num)
    for i in range(len(K)):
        if K[i]>student_num:
            continue
        id_0 = bisect.bisect_left(sum_arr,student_num-K[i]+1)
        now = key_arr[id_0-1]
        lef = student_num-K[i]+1-sum_arr[id_0-1]
        bit = bit_arr[id_0-1]
        # print (now,lef,bit)
        now += int(lef/bit)
        if lef and lef%bit==0:
            now -= 1
        S += now*(i+1)

    print ("Case #{}: {}".format(case, S))