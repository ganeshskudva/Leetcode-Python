# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # If the root is None (tree is empty), return None
        if not root:
            return root

        # Helper function to find the minimum value node in the right subtree
        def find_min(node):
            # The minimum value is the leftmost node
            while node.left:
                node = node.left
            return node
        
        # Recursive case: key is less than the root's value, search in the left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # Recursive case: key is greater than the root's value, search in the right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # If the key matches the root's value, this is the node to be deleted
        else:
            # Case 1: Node has no left child, return the right subtree (can be None or valid)
            if not root.left:
                return root.right
            
            # Case 2: Node has no right child, return the left subtree
            elif not root.right:
                return root.left
            
            # Case 3: Node has two children
            # Find the smallest node in the right subtree (in-order successor)
            min_node = find_min(root.right)
            
            # Replace the value of the node to be deleted with the in-order successor's value
            root.val = min_node.val
            
            # Delete the in-order successor (which is guaranteed to have at most one child)
            root.right = self.deleteNode(root.right, root.val)
        
        # Return the updated root after deletion
        return root

# Time Complexity (TC): O(h), where h is the height of the binary search tree.
# In a balanced BST, the time complexity is O(log n) due to halving the search space at each level.
# In the worst case (skewed tree), it could be O(n), where n is the number of nodes.

# Space Complexity (SC): O(h), where h is the height of the tree.
# This accounts for the recursion stack, which can reach O(log n) for a balanced tree
# and O(n) in the worst case for a skewed tree.
