def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    def re_wb(ss,wordDict,result):
        if len(ss) == 0:
            return True
        if (result[len(ss)]==1):
            return True
        if (result[len(ss)]==-1):
            return False
        ans = False
        for ww in wordDict:
            print ('for',ss,ww)
            if len(ww) > len(ss):
                continue
            n = len(ww)
            if ss[0:n] == ww:
                ans = ans or re_wb(ss[n:],wordDict,result)
        if ans:
            result[len(ss)] = 1
        else:
            result[len(ss)] = -1
        return ans

    result = [0]*(len(s)+1)
    
    return re_wb(s,wordDict,result)


s = "abcd"

wordDict = ["a","abc","b","cd"]
wordBreak(s, wordDict)