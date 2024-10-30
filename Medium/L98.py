# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to validate BST with min and max boundaries
        def solve(node, min_node=None, max_node=None):
            # Base case: if the current node is None, it's a valid BST subtree
            if not node:
                return True
            
            # Check if the current node value violates the BST property with min and max bounds
            if min_node and node.val <= min_node.val:
                return False
            if max_node and node.val >= max_node.val:
                return False
            
            # Recursively validate left and right subtrees with updated bounds
            return solve(node.left, min_node, node) and solve(node.right, node, max_node)

        # Start validation from the root
        return solve(root)

# Time Complexity (TC): O(n), where n is the number of nodes in the tree.
# The function visits each node once, performing constant-time operations at each step.

# Space Complexity (SC): O(h), where h is the height of the tree.
# This is due to the recursion stack, which reaches O(log n) for balanced trees
# and O(n) for skewed trees (worst case).

# iterative
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Base case: if the tree is empty, it's a valid BST
        if not root:
            return True
        
        # Initialize a stack for iterative in-order traversal and a variable to store previous node
        st, prev = [], None

        # Iterate through the tree
        while root or st:
            # Traverse the left subtree
            while root:
                st.append(root)
                root = root.left
            
            # Pop the node from the stack to process it
            root = st.pop()
            
            # If previous node exists and its value is greater than or equal to current node's value,
            # then it's not a valid BST
            if prev and root.val <= prev.val:
                return False
            
            # Update the previous node to the current node
            prev = root
            
            # Move to the right subtree
            root = root.right

        # If no violations of BST properties are found, return True
        return True

# Time Complexity (TC): O(n), where n is the number of nodes in the tree,
# because each node is visited once in an in-order traversal.

# Space Complexity (SC): O(h), where h is the height of the tree,
# due to the stack used for traversal. In the worst case (unbalanced tree), SC could be O(n).


