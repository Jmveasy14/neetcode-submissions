class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        visited = set()
        def dfs(curr_r,curr_c):
            if (curr_r,curr_c) not in visited and 0 <= curr_r < row and 0 <= curr_c < col and grid[curr_r][curr_c] == '1':
                visited.add((curr_r,curr_c))
                dfs(curr_r+1,curr_c)
                dfs(curr_r-1,curr_c)
                dfs(curr_r,curr_c+1)
                dfs(curr_r,curr_c-1)



        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    count +=1 

        return count

