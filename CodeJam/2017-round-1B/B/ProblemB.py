import fileinput
import numpy as np
import math

f = fileinput.input()
def input():
    return f.readline()

def judge(numList):
    return 
T = int(input())
for case in range(1, T+1):
    data= [int(x) for x in input().split()]
    #print (data)
    num_R_BY = [data[1],data[4]]
    num_Y_RB = [data[3],data[6]]
    num_B_RY = [data[5],data[2]]
    left_RYB = [data[1]-data[4],data[3]-data[6],data[5]-data[2]]
    #print (left_RYB)
    if (num_B_RY[0] <= num_B_RY[1] and num_B_RY[1] != 0) or (num_R_BY[0] <= num_R_BY[1] and num_R_BY[1] != 0) or (num_Y_RB[0] <= num_Y_RB[1] and num_Y_RB[1] != 0):
        tmp = 0
        if (num_B_RY[1] == 0):
            tmp += 1
        if (num_R_BY[1] == 0):
            tmp += 1
        if (num_Y_RB[1] == 0):
            tmp += 1
        if (tmp == 2 and num_B_RY[0] == num_B_RY[1] and num_R_BY[0] == num_R_BY[1] and num_Y_RB[0] == num_Y_RB[1]):
            strtmp = "R"*int(data[1]>0) + "O"*int(data[2]>0) + "Y"*int(data[3]>0) + "G"*int(data[4]>0) + "B"*int(data[5]>0) + "V"*int(data[6]>0)
            strAns = strtmp*(int(data[0]/2))
            print ("Case #{}: {}".format(case, strAns))
            continue
        else:
            strtmp = "IMPOSSIBLE"
            print ("Case #{}: {}".format(case, strtmp))
            #print ("error")
            continue
    
    if ((left_RYB[0] > left_RYB[1]+left_RYB[2]) or (left_RYB[1] > left_RYB[0]+left_RYB[2]) or (left_RYB[2] > left_RYB[1]+left_RYB[0])):
        strtmp = "IMPOSSIBLE"
        print ("Case #{}: {}".format(case, strtmp))
        continue
    
    str_R = "R"
    for by in range(num_R_BY[1]):
        str_R += "GR"
    str_Y = "Y"
    for by in range(num_Y_RB[1]):
        str_Y += "VY"
    str_B = "B"
    for by in range(num_B_RY[1]):
        str_B += "OB"

    dict_RYB = {"R": left_RYB[0],"Y": left_RYB[1],"B": left_RYB[2]}
    maxCol = max(dict_RYB,key=dict_RYB.get)
    
    minCol = min(dict_RYB,key=dict_RYB.get)
    if maxCol==minCol:
        minCol = "Y"
    tmp = ["R","Y","B"]
    tmp.remove(maxCol)
    tmp.remove(minCol)
    assert len(tmp) == 1
    midCol = tmp[0]
    colSort = [maxCol, midCol, minCol]
    maxnum = dict_RYB[maxCol]
    midnum = dict_RYB[midCol]
    minnum = dict_RYB[minCol]

    #print (maxCol,midCol,minCol)
    #print (maxnum,midnum,minnum)

    tmp1 = maxnum - minnum
    tmp2 = midnum - tmp1
    tmp3 = minnum - tmp2

    #print (tmp1,tmp2,tmp3)

    strtmp = ""
    for i in range(tmp2):
        strtmp += maxCol+midCol+minCol
    for i in range(tmp1):
        strtmp += maxCol+midCol
    for i in range(tmp3):
        strtmp += maxCol+minCol
    #print (strtmp)

    indexM = [0,0,0]
    #print (midCol)
    indexM[0] = strtmp.find(maxCol)
    indexM[1] = strtmp.find(midCol)
    indexM[2] = strtmp.find(minCol)
    assert indexM[0] == 0
    addStr = ["","",""]
    for i in range(3):
        if colSort[i] == "R":
            addStr[i] += str_R
        if colSort[i] == "Y":
            addStr[i] += str_Y
        if colSort[i] == "B":
            addStr[i] += str_B
    strAns = ""
    #print (addStr)
    #print (indexM)
    if indexM[2] == -1:
        strAns += addStr[0] + strtmp[indexM[0]+1:indexM[1]] + addStr[1] + strtmp[indexM[1]+1:]
    else:
        strAns += addStr[0] + strtmp[indexM[0]+1:indexM[1]] + addStr[1] + strtmp[indexM[1]+1:indexM[2]] + addStr[2] + strtmp[indexM[2]+1:]
    
    #print (strAns)
    assert len(strAns) == data[0]

    print ("Case #{}: {}".format(case, strAns))

        
