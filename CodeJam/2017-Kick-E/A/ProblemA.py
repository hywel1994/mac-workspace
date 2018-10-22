import fileinput
import numpy as np
import math

f = fileinput.input()
def input():
    return f.readline()

T = int(input())
for case in range(1, T+1):
    Data= input().strip('\n')
    print (Data)
    
    

    #print ("Case #{}: {}".format(case, data))