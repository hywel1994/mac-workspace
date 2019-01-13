def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    
    def function(wordDict, map_dict, s):
        if s in map_dict.keys():
            return map_dict[s]
        if s == '':
            return [""]
        data = []
        for i in range(len(wordDict)):
            len_word = len(wordDict[i])
            if wordDict[i] == s[0:len_word]:
                ans = function(wordDict, map_dict,s[len_word:])
                print ('ans',ans)
                # if ans == []:
                #     data += [wordDict[i]]
                # else:
                for a in ans:
                    if a: 
                        data += [wordDict[i]+' '+a]
                        print ([wordDict[i]+' '+a])
                    else:
                        data += [wordDict[i]]
                        print ([wordDict[i]])
        map_dict[s] = data
        print (map_dict)
        return data
                    
    map_dict = {}
    ans = function(wordDict,map_dict,s)
    return ans

s = "catsanddog"

wordDict = ["cats","dog","sand","and","cat"]
wordBreak(s, wordDict)