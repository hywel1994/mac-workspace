import fileinput
import numpy as np
import math

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
    sum = 0
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            for k in range(j+1,len(data)):
                if data[k] == data[i]*data[j] or data[j] == data[i]*data[k] or data[i] == data[j]*data[k]:
                    sum += 1
                    #print (data[i],data[j],data[k])

    print ("Case #{}: {}".format(case, sum))