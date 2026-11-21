class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = set()

        def dfs(row,col):
            if 0 <= row < rows and 0<= col < cols and (row,col) not in visited and grid[row][col] == "1":
                visited.add((row,col))
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row,col-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    count+=1
        
        return count
        