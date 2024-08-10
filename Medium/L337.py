# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = defaultdict(int)

        @cache
        def solve(node):
            if not node:
                return 0
            if node in dp:
                return dp[node]
            val = 0

            # If left child exists, add the grandchildren's values
            if node.left:
                val += solve(node.left.left) + solve(node.left.right)

            # If right child exists, add the grandchildren's values
            if node.right:
                val += solve(node.right.right) + solve(node.right.left)

            # Choose between robbing the current node or not
            val = max(val + node.val, solve(node.left) + solve(node.right))
            dp[root] = val

            return val

        return solve(root)
