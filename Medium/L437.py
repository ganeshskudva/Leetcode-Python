# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        def solve(node, curr_sum=0):
            if not node:
                return 0
            curr_sum += node.val
            res = 0
            if (curr_sum - targetSum) in dp:
                res = dp[curr_sum - targetSum]
            dp[curr_sum] += 1

            res += solve(node.left, curr_sum) + solve(node.right, curr_sum)
            if curr_sum in dp:
                dp[curr_sum] -= 1

            return res

        return solve(root)
