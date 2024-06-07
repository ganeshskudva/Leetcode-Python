# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if not node:
                return 0
            left_height = solve(node.left)
            if left_height == -1:
                return left_height
            right_height = solve(node.right)
            if right_height == -1:
                return right_height
            
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        
        return solve(root) != -1
