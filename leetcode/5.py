def canIWin(maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        def canWin(length,total,used,m):
            if used in m.keys(): return m[used]
            for i in range(length):
                cur = 1<<i
                if (cur & used) == 0:
                    
                    if total<= i+1 or (not canWin(length,total-i-1, cur|used,m)):
                        print (bin(used))
                        print ('True')
                        m[used] = True
                        return True
                    else:
                        m[used] = False
            print (bin(used))
            print ('False')       
            m[used] = False
            return False
        
        m = {}
        if maxChoosableInteger>=desiredTotal:
            return True
        if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
            return False
        ans = canWin(maxChoosableInteger,desiredTotal,0,m)
        print ('ans = ', ans)
        return ans



canIWin(6,10)