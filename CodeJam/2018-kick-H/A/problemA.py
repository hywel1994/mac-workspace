import fileinput
import numpy as np
import math
import bisect

f = fileinput.input()
def input():
    return f.readline()

T = int(input())
for case in range(1, T+1):
    N,P= [int(x) for x in input().split()]
    data = [input().replace('\n', '') for i in range(P)]
    #$print (data)
    data.sort()
    need = [1]*P
    #print (data)
    for i in range(1,P):
        if data[i].startswith(data[i-1]):
            data[i] = data[i-1]
            need[i] = 0
    sum_ans = 2**N
    for i in range(P):
        #print (sum_ans)
        #print(len(data[i]))
        if need[i] == 1:
            sum_ans -= 2**(N-len(data[i]))
    print ("Case #{}: {}".format(case, int(sum_ans)))