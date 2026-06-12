# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:  

    def isSametree(self,p,q) -> bool:
        if not q and not p:
            return True
        if (not q and p) or (not p and q):
            return False
        
        if q.val != p.val:
            return False
        
        return self.isSametree(q.left,p.left) and self.isSametree(q.right,p.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if self.isSametree(root,subRoot) is True:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        