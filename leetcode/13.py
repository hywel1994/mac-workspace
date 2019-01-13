def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    
    
    def two_sum(ans,find,target):
        if len(find) == 0:
            max_find = 0
        else:
            max_find = find[-1]
        i = max_find+1
        j = target-max_find-1
        while i<j and i <= 9:
            print (i,j)
            if j > 9:
                num = j
                j = 9
                i = num+i-9
                continue
            tmp = find[:]
            tmp.append(i)
            tmp.append(j)
            ans += [tmp]
            i += 1
            j -= 1
            
    def k_sum(ans,find,target,k_left):
        if k_left == 2:
            two_sum(ans,find,target)
            return
        if len(find) == 0:
            max_find = 1
        else:
            max_find = find[-1]
        if max_find < min(target//k_left,9):
            for i in range(max_find,min(target//k_left,9)+1):
                print (find,i,k_left)
                tmp = find[:]
                tmp.append(i)
                k_sum(ans,tmp,target-i,k_left-1)
            
    
    ans = []
    
    k_sum(ans,[],n,k)
    print (ans)
    return ans

combinationSum3(3,15)