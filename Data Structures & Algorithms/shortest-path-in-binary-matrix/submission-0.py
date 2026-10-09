from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        def bfs(row,col,distance):
            visited.add((row,col))

            queue = deque()
            queue.append((row,col,1))
            directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1),]
            while queue:
                r,c,dist = queue.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                        return dist
                #traversen graph while there are 0s until we reach one end to the other
                for dr, dc in directions:
                    new_r = dr+ r
                    new_c = dc + c
                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 0 and (new_r,new_c) not in visited:
                        visited.add((new_r,new_c))
                        queue.append((new_r,new_c,dist+1))
                        
            return -1
                        
        return bfs(0,0,0)


