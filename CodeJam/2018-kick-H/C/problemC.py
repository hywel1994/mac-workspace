import fileinput
import numpy as np
import math
import bisect


        
def gen_last_value(n,m):
    if n/2 < m:
        m = n - m
    sum1 = 1
    sum2 = 1
    for i in range(m):
        sum1 *= n-i
        sum2 *= 1+i
    ans1,ans2 = divmod(sum1,sum2)
    assert ans2 == 0
    ans0,ans1 = divmod(ans1,1000000007)
    # first = math.factorial(n)
    # #print "n:%s     value:%s"%(n, first)
    # second = math.factorial(m)
    # #print "n:%s     value:%s"%(m, second)
    # third = math.factorial((n-m))
    # #print "n:%s     value:%s"%((n-m), third)
    # ans2 = int(first/(second * third))%1000000007
    # assert ans2 == ans1 
    return ans1


f = fileinput.input()
def input():
    return f.readline()

T = int(input())
for case in range(1, T+1):
    N,M = [int(x) for x in input().split()] 
    #print (N,M)
    def p_cal(N,k):
        if k == 0:
            return int(math.factorial(2*N))%1000000007
        else:
            return int((2**k)*math.factorial(2*N-k))%1000000007

    sum_p = 0
    i_zhengfu = +1
    for i in range(M+1):
        if i == 0:
            sum_p += (i_zhengfu*p_cal(N,i))%1000000007
        else:
            sum_p += (i_zhengfu*p_cal(N,i)*gen_last_value(M,i))%1000000007
        i_zhengfu *= -1
    sum_p = sum_p%1000000007
    print ("Case #{}: {}".format(case, int(sum_p)))

    