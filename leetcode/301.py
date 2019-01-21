def removeInvalidParentheses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    def judge_error(s):
        left = 0
        right = 0
        for i in s:
            if i == "(": left +=1
            elif i == ")":
                if left>0: left -= 1
                else: right +=1
        return left, right
    
    ans = set()
    dict_e = set()
    def re_remove(s,left,right,ans,dict_e):
        
        if s in dict_e or s in ans:
            return
        if left == right == 0:
            print ('try' , s)
            ans_l, ans_r = judge_error(s)
            if ans_l == ans_r == 0:
                ans.add(s)
        else:
            for i in range(len(s)):
                if s[i] == '(' and left > 0:
                    re_remove(s[:i]+s[i+1:],left-1,right,ans,dict_e)
                    if i+1<len(s):
                        dict_e.add(s[:i]+s[i+1:])
                    else:
                        dict_e.add(s[:i])
                    print(s[:i]+s[i+1:])
                if s[i] == ')' and right > 0:
                    re_remove(s[:i]+s[i+1:],left,right-1,ans,dict_e)
                    if i+1<len(s):
                        dict_e.add(s[:i]+s[i+1:])
                    else:
                        dict_e.add(s[:i])
                    print(s[:i]+s[i+1:])

    
    left,right = judge_error(s)
    print (left,right)
    re_remove(s,left,right,ans,dict_e)

    print (ans)
    print(dict_e)
    return ans

s = "()())()"
removeInvalidParentheses(s)
