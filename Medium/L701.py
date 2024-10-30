# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the root is None (tree is empty), insert the value here
        if not root:
            return TreeNode(val)
        
        # Helper function to recursively find the correct position for insertion
        def solve(node):
            # Case 1: Insert val as the right child if node value is less than val and no right child exists
            if node.val < val and not node.right:
                node.right = TreeNode(val)
            # Case 2: Insert val as the left child if node value is greater than val and no left child exists
            elif node.val > val and not node.left:
                node.left = TreeNode(val)
            # Case 3: Continue searching in the left subtree if val is smaller than node value
            elif node.val > val:
                solve(node.left)
            # Case 4: Continue searching in the right subtree if val is greater than node value
            else:
                solve(node.right)
        
        # Start the recursive insertion from the root
        solve(root)
        
        # Return the root after insertion
        return root

# Time Complexity (TC): O(h), where h is the height of the tree.
# In a balanced BST, this is O(log n) due to the binary search behavior.
# In the worst case (skewed tree), this can be O(n), where n is the number of nodes.

# Space Complexity (SC): O(h), where h is the height of the tree.
# This accounts for the recursion stack, which can reach O(log n) for a balanced tree
# and O(n) in the worst case for a skewed tree.
