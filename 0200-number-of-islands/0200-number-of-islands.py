class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        
        # Depth First Search Solution

        # Use of another List[List] to mark all the islands as False visited
        visited = [[False for i in range(col)] for j in range(row)]

        # Thi method will mark the neighbour as visited and as well call the neighbours.
        def neighbour(g,v,i,j):

            if g[i][j] == "0" or v[i][j] == True:
                return
            
            v[i][j] = True
            if j - 1 >= 0:
                neighbour(g,v,i,j-1)
            if j + 1 < col:
                neighbour(g,v,i,j+1)
            if i - 1 >= 0:
                neighbour(g,v,i-1,j)
            if i + 1 < row:
                neighbour(g,v,i+1,j)


        # Looping over all the cells and if cell is already visited , continue else send it to neighbour method.

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1'and visited[i][j] == False:
                    neighbour(grid,visited,i,j)
                    res += 1
        return res