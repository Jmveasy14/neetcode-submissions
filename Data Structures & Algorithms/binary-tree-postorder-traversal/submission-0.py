# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        stack2 = []
        result = []
        while stack:
            current = stack.pop()
            stack2.append(current)

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        while stack2:
            current2 = stack2.pop()
            result.append(current2.val)

        return result
            
        