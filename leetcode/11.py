def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxTmp = 0
        n = len(height)
        lh = 0
        rh = n-1
        print (n,height[lh],height[r])
        while (lh<rh):
            maxTmp = max(maxTmp,min(height[lh],height[rh])*(rh-lh))
            if (height[lh]<height[rh]):
                lh += 1
            else:
                rh += 1
        
        return maxTmp

maxArea([1,8,6,2,5,4,8,3,7])