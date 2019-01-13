def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    string = list(string)
    num = [0]*52
    for i in range(len(s)):
        pose = string.index(s[i])
        print (pose)
        num[i] += 1
    print (num)
    ans = ''
    for i in range(52):
        ans += string[i]*num[i]
    return ans

frequencySort('tree')
