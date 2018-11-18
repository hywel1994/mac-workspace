def findKthLargest(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def QuickSort(myList,start,end,k):
            
            #判断low是否小于high,如果为false,直接返回
            if start < end:
                i,j = start,end
                #设置基准数
                base = myList[i]
                print(base, 'k=',k,'i=',i)
                while i < j:
                    #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
                    while (i < j) and (myList[j] <= base):
                        j = j - 1

                    #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
                    myList[i] = myList[j]

                    #同样的方式比较前半区
                    while (i < j) and (myList[i] >= base):
                        i = i + 1
                    myList[j] = myList[i]
                #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
                myList[i] = base

                #递归前后半区
                print (myList)
                
                if k-1 == i:
                    print(k,i,myList[i])
                    return myList[i]
                elif i > k-1:
                    print('i>k-1',start, i - 1, k)
                    return QuickSort(myList, start, i - 1, k)
                else:
                    print('i<k-1', j + 1, end, k)
                    return QuickSort(myList, j + 1, end, k)
        
        n = len(nums)
        ans = QuickSort(nums,0,n-1,k)

        return ans

a = findKthLargest([1],1)
print (a)