# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])

        if not root:
            return []
        result = []
        while queue:
            level_size = len(queue)
            curr_val = []

            for i in range(level_size):
                node = queue.popleft() 
                curr_val.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            result.append(curr_val)

        
        return result



        