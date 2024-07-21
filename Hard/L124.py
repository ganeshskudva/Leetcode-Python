# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')

        def solve(root):
            if not root:
                return 0

            left, right = max(solve(root.left), 0), max(solve(root.right), 0)
            self.maxi = max(self.maxi, root.val + left + right)

            return root.val + max(left, right)

        solve(root)
