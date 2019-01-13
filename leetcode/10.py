def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    def DecConversion(dec,k):
        # 递归调用进制数据转换函数
        print (dec,k)
        result = DecConversion(dec // k,k)
        # 输出转换后的结果
        return result + chr(dec % k+65)

    ans = DecConversion(n-1,26)
    print (ans)
    return ans

convertToTitle(28)