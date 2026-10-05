class Solution: 
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(node): 
            for j in range(n):
                if isConnected[node][j] == 1 and j not in visited:
                    visited.add(node)
                    dfs(j)

            pass

        for i in range(n):
           if i not in visited:
                provinces+=1
                dfs(i)


        return provinces 
