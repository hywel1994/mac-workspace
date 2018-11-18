def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxl = 0
        start = 0
        for i in range(n):
            print ("i=",i, " S= ", s[i-maxl: i+1])
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                print (">=1",s[i-maxl-1: i+1], "start= ",start,"maxl= ", maxl)
                start = i - maxl - 1
                maxl += 2
                print (">=1","start= ",start,"maxl= ", maxl)
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                print (">=0",s[i-maxl: i+1],"start= ",start,"maxl= ", maxl)
                start = i - maxl
                maxl += 1
                print (">=0","start= ",start,"maxl= ", maxl)
        return s[start: start + maxl]

def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        n = len(s)
        yu = n%(numRows*2-2)
        col = int(n/(numRows*2-2))*2
        if yu > 0:
            col += 2
        s = s + '#'*(numRows*2-2-yu)
        
        
        data = [['#' for i in range(col)] for i in range(numRows)]
        
        for i in range(col):
            if i%2 == 0:
                tmp = s[int((numRows*2-2)*(i/2)):int(numRows+(numRows*2-2)*(i/2))]
                for j in range(numRows):
                    data[j][i] = tmp[j]
            else:
                tmp = s[int(numRows+(numRows*2-2)*int(i/2)):int(2*numRows-2+(numRows*2-2)*int(i/2))]
                for j in range(numRows-2):
                    data[j+1][i] = tmp[j]
        
        text = ''
        for i in range(numRows):
             for j in range(col):
                    text += data[i][j]
        text = text.replace('#','')
        print (text)
        return text


convert('PAYPALISHIRING',3)
convert('PAYPALISHIRING',1)