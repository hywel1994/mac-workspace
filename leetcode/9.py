def ambiguousCoordinates(S):
    """
    :type S: str
    :rtype: List[str]
    """
    def find_0(s):
        i = 0
        j = len(s)
        while s[i] == '0':
            i += 1
        while s[j-1] == '0':
            j -= 1
        return i,len(s)-j
            
    S = S[1:-1]
    n = len(S)
    data = []
    print(n)
    for i in range(1,n):
        a_set = []
        b_set = []
        a = S[0:i]
        b = S[i:]
        a_judge = find_0(a)
        b_judge = find_0(b)
        print(a,b)
        if (not (a_judge[0]>0 and a_judge[1]>0 ) or (a_judge[0] == len(a) and a_judge[0] == 1) ) and (not (b_judge[0]>0 and b_judge[1]>0) or (b_judge[0] == len(b) and b_judge[0] == 1)):
            if (a_judge[0] == len(a) and a_judge[0] == 1):
                a_set += [a]
            elif a_judge[0]>0:
                a_set += [a[0]+'.'+a[1:]]
            elif a_judge[1]>0:
                a_set += [a]
            else:
                a_set += [a]
                for k in range(1,len(a)):
                    a_set += [a[0:k]+'.'+a[k:]]
                    
            if (b_judge[0] == len(b) and b_judge[0] == 1):
                b_set += [b]
            elif b_judge[0]>0:
                b_set += [b[0]+'.'+b[1:]]
            elif b_judge[1]>0:
                b_set += [b]
            else:
                b_set += [b]
                for k in range(1,len(b)):
                    b_set += [b[0:k]+'.'+b[k:]]
            
        for m in a_set:
            for n in b_set:
                data += ["("+m+","+n+")"]
    print (data)
    return data
                    

ambiguousCoordinates("(123)")