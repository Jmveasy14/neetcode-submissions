# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if (not q and p) or (not p and q):
            return False
        
        if q.val == p.val:

            left_child = self.isSameTree(q.left,p.left)
            right_child = self.isSameTree(q.right,p.right)
            
        if q.val != p.val:
            return False
        
        return left_child and right_child


        