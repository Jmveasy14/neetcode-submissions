class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0
        
        def dfs(node):
            visited.add(node)
            for j in range(len(isConnected)):
                if j not in visited and isConnected[node][j] == 1: 
                    dfs(j)
            
        for i in range(len(isConnected)):
            if i not in visited:
                provinces+=1
                dfs(i)
        
        return provinces