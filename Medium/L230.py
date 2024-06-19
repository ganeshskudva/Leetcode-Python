# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res, self.cnt = 0, k
        
        def solve(node):
            if not node:
                return 

            solve(node.left)
            self.cnt -= 1
            if self.cnt == 0:
                self.res = node.val
                return 
            solve(node.right)
            
        solve(root)
        return self.res
