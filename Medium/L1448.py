# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res, self.cnt = [], 0

        def solve(node, val=0):
            if not node:
                return
            if node.val >= val:
                self.cnt += 1

            solve(node.left, max(node.val, val))
            solve(node.right, max(node.val, val))

        solve(root, root.val)
        return self.cnt
