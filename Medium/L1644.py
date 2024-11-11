class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Array to keep track if nodes p and q are found in the tree
        nodes_found = [False] * 2

        # Helper function to perform DFS and find the LCA
        def solve(node):
            if not node:
                return None  # Return None if the current node is null

            # Recursively search in the left and right subtrees
            left, right = solve(node.left), solve(node.right)

            # Check if the current node is `p` or `q` and mark them as found
            if node == p:
                nodes_found[0] = True
                return node
            if node == q:
                nodes_found[1] = True
                return node

            # If both `left` and `right` are non-null, then `node` is the LCA of `p` and `q`
            if left and right:
                return node

            # Otherwise, return the non-null child if any, otherwise return None
            return left if left else right

        # Perform DFS starting from the root to find the LCA
        res = solve(root)
        
        # Ensure that both `p` and `q` were found in the tree
        return res if all(nodes_found) else None

# Time Complexity (TC): O(n), where n is the number of nodes in the tree.
# - We visit each node once in the recursive search, making the time complexity linear.

# Space Complexity (SC): O(h), where h is the height of the tree.
# - The recursion depth is determined by the height of the tree, requiring O(h) space for the call stack.
# - In the worst case, this could be O(n) for a skewed tree.
