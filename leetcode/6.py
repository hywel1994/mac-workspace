def kSmallestPairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    k1 = k2 = 0
    ans = []
    for i in range(k):
        if i>=len(nums1)*len(nums2):
            break
        if i==0:
            ans += [[nums1[k1],nums2[k2]]]
            continue
        print (k1,k2)
        if (k1+1 >= len(nums1)):
            k2 += 1
            ans += [[nums1[-1],nums2[k2]]]
        elif (k2+1 >= len(nums2)):
            k1 += 1
            ans += [[nums1[k1],nums2[-1]]]
        else:
            if nums1[k1+1]*nums2[k2] > nums1[k1]*nums2[k2+1]:
                k2 += 1
                ans += [[nums1[k1],nums2[k2]]]
            else:
                k1 += 1
                ans += [[nums1[k1],nums2[k2]]]
    return ans

kSmallestPairs([1,2,3],[1,2,3],10)