class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # Base case: if root is None, return an empty string
        if not root:
            return ""

        # Initialize a list to build the output string efficiently
        ret = []

        # Define recursive function to build the string representation
        def solve(root):
            # Append the current node's value to the result list
            ret.append(f'{root.val}')
            
            # If the node is a leaf, stop recursion here
            if not root.left and not root.right:
                return
            
            # If there is a left child, recurse into it and wrap in parentheses
            if root.left:
                ret.append("(")
                solve(root.left)
                ret.append(")")
            
            # If there is a right child but no left child, add empty parentheses for left
            if root.right:
                if not root.left:
                    ret.append("()")
                ret.append("(")
                solve(root.right)
                ret.append(")")
        
        # Start the recursive solution from the root
        solve(root)
        
        # Join the list of strings into the final output
        return ''.join(ret)

# Time Complexity (TC): O(n), where n is the number of nodes in the tree.
# The function visits each node once and appends its value or parentheses.

# Space Complexity (SC): O(h), where h is the height of the tree for the recursion stack.
# Additional space is used for the output string list `ret`, which will contain all nodes and parentheses.
# This space grows as O(n), where n is the number of nodes in the tree, in the worst case.
