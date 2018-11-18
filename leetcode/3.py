def pacificAtlantic(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if (len(matrix) == 0):
            return None
        m = len(matrix)
        n = len(matrix[0])
        print (m,n)
        pacific = [[0 for i in range(n)] for j in range(m)]
        atlantic = [[0 for i in range(n)] for j in range(m)]
        print (pacific)
        def dfsfunction(matrix,visited,pre,i,j):
            m = len(matrix)
            n = len(matrix[0])
            print (i,j)
            if (i<0 or i>=m or j<0 or j>=n):
                return
            if (visited[i][j] or matrix[i][j]<pre):
                return
            visited[i][j] = True
            print ('visit',i,j)
            dfsfunction(matrix,visited,matrix[i][j],i+1,j)
            dfsfunction(matrix,visited,matrix[i][j],i-1,j)
            dfsfunction(matrix,visited,matrix[i][j],i,j+1)
            dfsfunction(matrix,visited,matrix[i][j],i,j-1)
            return
        
        for i in range(m):
            dfsfunction(matrix,pacific,0,i,0)
            dfsfunction(matrix,atlantic,0,i,n-1)
        
        for j in range(n):
            dfsfunction(matrix,pacific,0,0,j)
            dfsfunction(matrix,atlantic,0,m-1,j)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if (pacific[i][j] and atlantic[i][j]):
                    ans += [[i,j]]
        
        return ans
    

a = [[1,1],[1,1],[1,1]]
pacificAtlantic(a)