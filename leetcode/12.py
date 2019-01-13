def findLongestWord(s, d):
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """
    
    def judge(source,target):
        while True:
            if len(target) == 0:
                return True
            if len(source) == 0:
                return False
            if source[-1] == target[-1]:
                source.pop()
                target.pop()
            else:
                source.pop()
    
    ans = ""
    for target_d in d:
        if judge(list(s)[::-1],list(target_d)[::-1]):
            if len(ans) < len(target_d):
                ans = target_d
            elif len(ans) == len(target_d) and ans > target_d:
                ans = target_d
    return ans

s = "aaa"
d = ["aaa","aa","a"]
findLongestWord(s, d)