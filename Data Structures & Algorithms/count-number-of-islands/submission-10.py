class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        count = 0

        def dfs(r,c):
            if not ((0 <= r < ROWS) and (0<= c < COLS) and (grid[r][c] == '1') and ((r,c) not in visited)):
                return
            visited.add((r,c))
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)


        for r in range (ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    count+=1
        
        return count

                

        