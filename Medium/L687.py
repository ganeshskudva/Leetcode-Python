# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def solve(node, val):
            if not node:
                return 0
            left, right = solve(node.left, node.val), solve(node.right, node.val)
            self.max_len = max(self.max_len, left + right)

            return 1 + max(left, right) if val == node.val else 0

        if not root:
            return 0
        solve(root, root.val)
        return self.max_len
