# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(node, tgt=0):
            if not node:
                return False
            if tgt == node.val and not node.left and not node.right:
                return True

            return solve(node.left, tgt - node.val) or solve(node.right, tgt - node.val)

        return solve(root, targetSum)
