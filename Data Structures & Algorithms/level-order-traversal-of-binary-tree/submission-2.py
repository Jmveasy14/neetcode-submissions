# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []
            queue = deque([root])
            levels = []

            while queue:
                current_levels = []
                level_size = len(queue)
                
                for i in range(level_size):
                    current = queue.popleft()
                    current_levels.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                levels.append(current_levels)

            return levels
