# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize the result and a counter for the kth element
        self.res, self.cnt = 0, k
        
        def solve(node):
            if not node:  # Base case: If the node is None, return
                return 

            # In-order traversal: Process left subtree
            solve(node.left)
            
            # Decrement the counter and check if it's the kth element
            self.cnt -= 1
            if self.cnt == 0:  # Found the kth smallest element
                self.res = node.val
                return 
            
            # In-order traversal: Process right subtree
            solve(node.right)
            
        solve(root)
        return self.res

# Time Complexity (TC):
# - The in-order traversal visits each node once in a binary search tree.
# - Thus, the time complexity is O(n), where n is the number of nodes in the tree.
#   In the best case, if k is small, we may terminate early, but the worst case is O(n).

# Space Complexity (SC):
# - The space complexity is O(h), where h is the height of the tree.
# - This is due to the recursive call stack, which can go as deep as the tree's height.
#   In a balanced tree, h = O(log n); in a skewed tree, h = O(n).

