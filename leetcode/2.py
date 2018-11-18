def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        stark = []
        for i in s:
            print (i)
            if i == '(' or i == '[' or i == '{':
                stark.append(i)
            else:
                if len(stark):
                    tmp = stark.pop()
                    print (~((i == ')' and tmp == '(') or (i == ']' and tmp == '[') or (i == '}' and tmp == '{')))
                    if not((i == ')' and tmp == '(') or (i == ']' and tmp == '[') or (i == '}' and tmp == '{')):
                        print ('F')
                        return False
                else:
                    return False
        return True

print (isValid('()'))