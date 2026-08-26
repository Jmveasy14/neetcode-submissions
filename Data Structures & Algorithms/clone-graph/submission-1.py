"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
                return None
        cloned = {}

        def dfs(curr):
            
            if curr in cloned:
                return cloned[curr]

            copy = Node(curr.val)

            cloned[curr] = copy

            #clone all neighbors and connect them to the copied node
            for n in curr.neighbors:
                copy.neighbors.append(dfs(n))

            return copy
        return dfs(node)
        
        