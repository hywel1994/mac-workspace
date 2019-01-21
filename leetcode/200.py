def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def visit_island(grid,visit,i,j):
        if i >= len(grid):
            return
        if j >= len(grid[0]):
            return
        if grid[i][j] == "1" and not visit[i][j]:
            visit[i][j] = 1
            visit_island(grid,visit,i+1,j)
            visit_island(grid,visit,i,j+1)
    
    visit = [[0]*len(grid[0]) for i in range(len(grid))]
    num = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and not visit[i][j]:
                visit_island(grid,visit,i,j)
                print (visit)
                num += 1
    print (num)
    return num

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
numIslands(grid)