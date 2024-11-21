# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Dictionary to store cumulative sums and their frequencies
        dp = defaultdict(int)
        dp[0] = 1  # Base case: A path starting at the root with targetSum
        
        def solve(node, curr_sum=0):
            if not node:
                return 0  # No valid path in an empty subtree
            
            # Add the current node's value to the cumulative sum
            curr_sum += node.val
            
            # Initialize result count for this node
            res = 0
            
            # Check if there is a valid path ending at this node
            if (curr_sum - targetSum) in dp:
                res = dp[curr_sum - targetSum]
            
            # Increment the count of the current cumulative sum in dp
            dp[curr_sum] += 1
            
            # Recur for left and right subtrees
            res += solve(node.left, curr_sum)
            res += solve(node.right, curr_sum)
            
            # Backtrack: Remove the current cumulative sum from dp
            dp[curr_sum] -= 1
            
            return res
        
        # Start the recursive function
        return solve(root)

# Time Complexity (TC): O(n)
# - Each node is visited exactly once, where n is the number of nodes in the tree.
# - Dictionary operations (lookup, insertion, and deletion) are O(1) on average.
# Total: O(n).

# Space Complexity (SC): O(h + k)
# - O(h): Maximum depth of recursion stack, where h is the height of the tree.
# - O(k): Space for the dictionary `dp`, where k is the number of unique cumulative sums.
# In the worst case, h = n (skewed tree) and k = n (unique sums for each node).
# Total: O(h + k).

