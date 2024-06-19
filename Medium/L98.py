# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(node, min_node=None, max_node=None):
            if not node:
                return True
            if min_node and node.val <= min_node.val:
                return False
            if max_node and node.val >= max_node.val:
                return False
            return solve(node.left, min_node, node) and solve(node.right, node, max_node)
        return solve(root)
