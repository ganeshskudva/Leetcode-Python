class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Initialize variables to keep track of previous node value, current count,
        # maximum frequency of any value, and the list of mode(s).
        self.prev = None  # Tracks the value of the previous node
        self.count = 0    # Tracks the current frequency of the current value
        self.max_count = 0  # Stores the maximum frequency encountered
        self.modes = []   # Stores all values with maximum frequency

        def inorder(node):
            # Perform in-order traversal (left -> root -> right)
            if not node:
                return
            
            # Recurse on the left subtree
            inorder(node.left)
            
            # Process the current node
            if self.prev == node.val:
                # Increment the count if the current value matches the previous value
                self.count += 1
            else:
                # Reset count to 1 for a new value
                self.count = 1
            
            # Update modes and max_count if necessary
            if self.count > self.max_count:
                # Found a new maximum frequency; reset modes
                self.max_count = self.count
                self.modes = [node.val]
            elif self.count == self.max_count:
                # If the frequency matches max_count, add to modes
                self.modes.append(node.val)
            
            # Update the previous node value
            self.prev = node.val
            
            # Recurse on the right subtree
            inorder(node.right)
        
        # Start the in-order traversal from the root
        inorder(root)

        # Return the list of mode(s)
        return self.modes

# Time Complexity:
# - The in-order traversal visits each node exactly once.
# - Thus, the time complexity is O(n), where n is the number of nodes in the tree.

# Space Complexity:
# - The recursion stack depth is proportional to the height of the tree.
# - For a balanced tree, the height is O(log n), so the space complexity is O(log n).
# - For a skewed tree, the height is O(n), so the space complexity is O(n).
# - There is no additional space used for storing node frequencies, making it efficient.
