# recursive
class Solution:
    def __init__(self):
        # Initialize self.prev to None, ensuring it retains its value across recursive calls
        # This tracks the last processed node in the flattened tree.
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        # Base case: if the node is None, return immediately
        if not root:
            return
        
        # Recursively flatten the right subtree first (post-order traversal: right -> left -> root)
        self.flatten(root.right)
        
        # Recursively flatten the left subtree
        self.flatten(root.left)
        
        # Set the current node's right child to the previously processed node (self.prev)
        root.right = self.prev
        # Set the current node's left child to None, as required for the flattened list
        root.left = None
        
        # Update self.prev to the current node, making it the "previous" node for the next call
        self.prev = root

# Time Complexity (TC):
# - Each node is visited once in the tree, making the time complexity O(N), where N is the number of nodes in the tree.
# - This is due to the post-order traversal (right -> left -> root) on each node exactly once.

# Space Complexity (SC):
# - The space complexity is O(H), where H is the height of the tree, due to the recursion stack.
# - In the worst case (for a completely unbalanced tree), this can be as high as O(N).
# - In the best case (for a balanced tree), the space complexity would be O(log N).


# iterative
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Traverse the tree while root is not None
        while root:
            # If the current node has both left and right children
            if root.left and root.right:
                # Find the rightmost node in the left subtree
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                # Connect the right subtree of the current node to the rightmost node of the left subtree
                tmp.right = root.right
            
            # If the current node has a left child, make it the right child
            if root.left:
                root.right = root.left
            
            # Set the left child to None and move to the right child
            root.left, root = None, root.right

# Time Complexity (TC):
# - Each node in the tree is visited once, so the overall time complexity is O(N),
#   where N is the number of nodes in the tree.
# - For each node, we may traverse the left subtree to find the rightmost node, which 
#   takes O(H) time in the worst case for each node, where H is the height of the tree.
# - However, the overall traversal across all nodes is O(N) because each link modification
#   and subtree connection only happens once.

# Space Complexity (SC):
# - The space complexity is O(1) since this approach modifies the tree in place without 
#   using any additional data structures.
# - There is no recursion stack since this is an iterative solution, and we only use a few
#   temporary variables, making it a constant-space solution.
