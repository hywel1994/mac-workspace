def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    num_copy = nums.copy()
    num_copy.sort()
    
    start = 0
    end = len(nums)
    for i in range(len(nums)):
        print (nums[i],num_copy[i])
        if nums[i]==num_copy[i]:
            start +=1
            print (start)
        else:
            break
    for i in range(len(nums))[::-1]:
        print (nums[i],num_copy[i])
        if nums[i]==num_copy[i]:
            end +=1
            print (end)
        else:
            break
    
    return end - start

nums = [2,6,4,8,10,9,15]
findUnsortedSubarray(nums)