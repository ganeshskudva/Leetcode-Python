# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def solve(node):
            if not node:
                return -1
            lvl = 1 + max(solve(node.left), solve(node.right))
            if len(res) < lvl + 1:
                res.append([])
            res[lvl].append(node.val)
            return lvl

        solve(root)
        return res
