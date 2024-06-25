# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:       
        def solve(node):
            if not node:
                return 
            solve(node.right)
            node.val += self.tot
            self.tot = node.val
            solve(node.left)

        self.tot = 0
        solve(root)
        return root
