# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Initialize variables for minimum difference and previous node in order
        minimum, prev = float("inf"), None

        # In-order traversal function with minimum and prev as parameters
        def in_order(node, minimum, prev):
            if not node:  # Base case: if node is None, return current minimum and prev
                return minimum, prev
            
            # Traverse the left subtree, updating minimum and prev
            minimum, prev = in_order(node.left, minimum, prev)
            
            # Update minimum difference if prev node exists
            if prev:
                minimum = min(minimum, node.val - prev.val)
            prev = node  # Update prev to current node
            
            # Traverse the right subtree, updating minimum and prev
            return in_order(node.right, minimum, prev)

        # Start in-order traversal from the root
        minimum, _ = in_order(root, minimum, prev)
        
        return minimum

# Time Complexity (TC): O(n), where n is the number of nodes in the binary search tree.
# The function performs an in-order traversal, visiting each node once, resulting in O(n) time.

# Space Complexity (SC): O(h), where h is the height of the binary search tree.
# This is due to the recursion stack. For a balanced BST, this is O(log n).
# In the worst case (e.g., a skewed tree), the space complexity can be O(n).
