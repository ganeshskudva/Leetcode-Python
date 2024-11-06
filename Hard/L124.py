# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize maxi with negative infinity to store the maximum path sum found
        self.maxi = float('-inf')
        
        # Helper function to calculate maximum path sum recursively
        def solve(root):
            # Base case: if the node is None, it contributes 0 to the path
            if not root:
                return 0
            
            # Recursive calls to get the maximum sum from left and right subtrees
            # If a subtree sum is negative, we ignore it by taking max with 0
            left = max(solve(root.left), 0)
            right = max(solve(root.right), 0)
            
            # Update the global maximum path sum, considering the current node as the highest node in the path
            self.maxi = max(self.maxi, root.val + left + right)
            
            # Return the maximum path sum including the current node and one of its subtrees
            return root.val + max(left, right)
        
        # Call the solve function starting from the root node
        solve(root)
        
        # Return the maximum path sum found
        return self.maxi

# Time Complexity (TC): O(N), where N is the number of nodes in the tree, as each node is visited once.
# Space Complexity (SC): O(H), where H is the height of the tree, due to the recursion stack. 
# In the worst case (skewed tree), H = N. In the best case (balanced tree), H = log(N).

