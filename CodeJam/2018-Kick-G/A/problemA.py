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
    data = [int(x) for x in input().split()] 
    #print (data)
# data = [5,2,4,6,3,1]
# case = 1
    data.sort(reverse=True)
    sum_ans = 0
    ans = {}
    assert N == len(data)
    for num in range(N):
        target = data[num]   
        i = num+1
        j = N-1
        while i<j:
            tmp = data[i]*data[j]
            if tmp == target:
                if data[i] == data[j]:
                    sum_ans += (j-i+1)*(j-i)/2
                    break
                else:
                    same_i = same_j = 1
                    while data[i] == data[i+1]:
                        i += 1
                        same_i +=1
                    while data[j] == data[j-1]:
                        j -= 1
                        same_j +=1
                    sum_ans += same_i * same_j
                    i += 1
                    j -= 1
            elif tmp > target:
                i += 1
            else:
                j -= 1
    data.sort()
    id_0 = bisect.bisect_right(data,0)
    if id_0 > 0:
        num_0 = id_0
        sum_ans += (N-num_0)*(num_0-1)*num_0/2

    print ("Case #{}: {}".format(case, int(sum_ans)))