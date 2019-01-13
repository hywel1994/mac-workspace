def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    heights.append(0)
    stack = []
    i = 0
    result = 0
    while i<len(heights):
        print (stack)
        if not stack or heights[stack[-1]]<heights[i]:
            stack.append(i)
            i+=1
        else:
            num = stack.pop(-1)
            result = max(result,heights[num]*(i-stack[-1]-1 if stack else i))
            print(i,result)
    return result


height = [2,1,5,6,2,3]
largestRectangleArea(height)

