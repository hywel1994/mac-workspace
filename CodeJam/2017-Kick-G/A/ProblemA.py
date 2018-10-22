import fileinput
import numpy as np
import math
import sys
 
sys.setrecursionlimit(1000000)

f = fileinput.input()
def input():
    return f.readline()

def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

def calrate(A,P):
    mod = []

    gcdAP = gcd(A,P)
    atmp = A/gcdAP
    ptmp = P/gcdAP
    tmpmod1 = atmp%ptmp
    tmpmod = tmpmod1
    mod += [tmpmod]
    while True:
        tmpmod = (tmpmod*tmpmod1)%ptmp
        
        if tmpmod in mod:
            break
        else:
            mod += [tmpmod]
    return [x*gcdAP for x in mod]

def pow(a, n, p):
    if (n == 0) :
        return 1

    pow_half = pow(a, n / 2, p)
    pow_half_sq = (pow_half  * pow_half) % p # again, multiplication is associative modulo p
    if n % 2 == 0:
        return pow_half_sq
    else:
        return (pow_half_sq * a) % p

T = int(input())
for case in range(1, T+1):
    A, N, P= [int(x) for x in input().split()]
    #print (A,N,P)
    
    # Amod = calrate(A,P)
    # #print (Amod)
    # if N > len(Amod):
    #     ans = Amod[-1]
        
    # else:
    #     value = math.factorial(N)
    #     Nmod = value%len(Amod)
    #     ans = Amod[Nmod-1]
    #     #print (Amod,N)
    # 

    ans = A % P
    for i in range(2, N):
        ans = pow(ans, i, P)

    print ("Case #{}: {}".format(case, ans))