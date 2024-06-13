# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def isSame(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            
            if s.val != t.val:
                return False
            
            return isSame(s.left, t.left) and isSame(s.right, t.right)
            
        if isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
