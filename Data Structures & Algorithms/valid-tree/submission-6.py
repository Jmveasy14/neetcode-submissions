class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False

        
        adj = {i: [] for i in range(n)}
        visited = set()
        for item1,item2 in edges:
            adj[item1].append(item2)
            adj[item2].append(item1)

        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for val in adj[node]:
                if val == parent:
                    continue

                if not dfs(val,node):
                    return False

            return True

        return dfs(0,-1) and len(visited) == n