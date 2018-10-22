import fileinput
import numpy as np

f = fileinput.input()
def input():
    return f.readline()

def find_left(string_raw, index_one):
    if index_one == 0:
        return "?"
    else:
        return string_raw[index_one - 1]

def find_right(string_raw, index):
    #print ("string",string_raw)
    #rint ("index",index)
    len1 = np.size(string_raw)
    for i in range(len1):
        pose = np.argwhere(index == i)
        #print ("pose",type(pose))
        if np.size(pose) == 0:
            return string_raw[i]


T = int(input())
for case in range(1, T+1):
    R,C = [int(x) for x in input().split()]
    cashiers = [input() for i in range(R)]
    for i in range(R):
        cashiers[i] = list(cashiers[i].strip())
    cashiers = np.array(cashiers)
    
    spare = []
    for i in range(R):
        pose = np.argwhere(cashiers[i] == "?")
        #print (pose)
        if np.size(pose) == C:
            spare += [i]
        elif np.size(pose) != 0:
            for j in range(np.size(pose)):

                tmp = find_left(cashiers[i],pose[j])
                if tmp == "?":
                    tmp = find_right(cashiers[i],pose)
                cashiers[i][pose[j]] = tmp
            #     if cashiers[i][j] == "?":
            #         cashiers[i]
            #     cashiers[]
    
    if len(spare) != 0:
        spare = np.array(spare)
        #print (spare)
        for i in range(np.size(spare)):
            if spare[i] == 0:
                for i in range(R):
                    #print ("spare",spare)
                    pose = np.argwhere(spare == i)
                    #print ("pose",type(pose))
                    if np.size(pose) == 0:
                        #print ("pose",pose)
                        cashiers[0] =  cashiers[i]
                        break
            else:
                cashiers[spare[i]] = cashiers[spare[i]-1] 
    print ("case #{}:".format(case))
    
    for i in range(R):
        solustion = ""
        for j in range(C):
            solustion += cashiers[i][j]
        print("{}".format(solustion))
