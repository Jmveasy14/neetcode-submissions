class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i: [] for i in range(n)}
        visited = set()
        count = 0
        for item1,item2 in edges:
            adj[item1].append(item2)
            adj[item2].append(item1)

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)

        return count

