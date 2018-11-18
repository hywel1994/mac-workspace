import fileinput
import numpy as np
import math

import sys
 
sys.setrecursionlimit(1000000)

global N,M,E,SR,SC,TR,TC,data,ans



f = fileinput.input()
def input():
    return f.readline()


T = int(input())
for case in range(1, T+1):
    N,M,E,SR,SC,TR,TC = [int(x) for x in input().split()]
    data = [[int(x) for x in input().split()] for i in range(N)]
    dis = [[-float('INF')] * M for i in range(N)]
    dis[SR-1][SC-1] = E
    visit_v = [[0] * M for i in range(N)]
    edge_row = [[0] * (M-1) for i in range(N)]
    edge_col = [[0] * M for i in range(N-1)]
    visit_row = [[0] * (M-1) for i in range(N)]
    visit_col = [[0] * M for i in range(N-1)]
    for i in range(N):
        for j in range(M):
            if data[i][j] != 0:
                if N > 1:
                    if i == 0:
                        edge_col[i][j] = data[i][j]/2
                    elif i == N-1:
                        edge_col[i-1][j] = data[i][j]/2
                    else:
                        edge_col[i-1][j] = data[i][j]/2
                        edge_col[i][j] = data[i][j]/2
                if M > 1:
                    if j == 0:
                        edge_row[i][j] = data[i][j]/2
                    elif j == M-1:
                        edge_row[i][j-1] = data[i][j]/2
                    else:
                        edge_row[i][j] = data[i][j]/2
                        edge_row[i][j-1] = data[i][j]/2


    def dij():
        #chushihua
        for i in range(M*N):
            max_num = -float('INF')
            k = 0
            x_min = -1
            y_min = -1
            for j in range(M*N):
                x,y = divmod(j,M)
                if not visit_v[x][y] and dis[x][y] > max_num:
                    max_num = dis[x][y]
                    x_min = x
                    y_min = y
            visit_v[x_min][y_min] = 1
            if x_min>0:
                if not visit_v[x_min-1][y_min] and edge_col[x_min-1][y_min] > -100000/2 and max_num+edge_col[x_min-1][y_min]>dis[x_min-1][y_min]:
                    dis[x_min-1][y_min] = max_num+edge_col[x_min-1][y_min]
            if x_min<N-1:
                if not visit_v[x_min+1][y_min] and edge_col[x_min][y_min] > -100000/2 and max_num+edge_col[x_min][y_min]>dis[x_min+1][y_min]:
                    dis[x_min+1][y_min] = max_num+edge_col[x_min][y_min]
            if y_min>0:
                if not visit_v[x_min][y_min-1] and edge_row[x_min][y_min-1] > -100000/2 and max_num+edge_row[x_min][y_min-1]>dis[x_min][y_min-1]:
                    dis[x_min][y_min-1] = max_num+edge_row[x_min][y_min-1] 
            if y_min<M-1:
                if not visit_v[x_min][y_min+1] and edge_row[x_min][y_min] > -100000/2 and max_num+edge_row[x_min][y_min]>dis[x_min][y_min+1]:
                    dis[x_min][y_min+1] = max_num+edge_row[x_min][y_min]


    dij()
    # print ("dis",dis)
    # print ('visit_v',visit_v)
    S = dis[TR-1][TC-1]
    if S<0:
        S = -1
    print ("Case #{}: {}".format(case, int(S)))