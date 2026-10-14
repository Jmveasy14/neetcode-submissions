class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        def dfs(r,c):
            if  (0<= r < rows) and (0<= c< cols) and (r,c) not in visited and grid[r][c] == '1':
                visited.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            else:
                return
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    count+=1

        return count