# Similar to LC 1644
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

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is either p, q, or None, return root
        # This indicates that we've found one of the nodes or reached a leaf
        if root == p or root == q or not root:
            return root

        # Recursively search for LCA in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If only one of left or right is non-null, return the non-null child
        if not left:
            return right
        elif not right:
            return left
        
        # If both left and right are non-null, root is the LCA
        return root

# Time Complexity (TC):
# - The function visits each node in the binary tree once, leading to O(N) complexity,
#   where N is the total number of nodes in the tree.

# Space Complexity (SC):
# - The space complexity depends on the recursion stack depth.
# - In the worst case (for a skewed tree), the recursion depth is O(N).
# - In the best/average case (for a balanced tree), the recursion depth is O(log N).
# - Therefore, the overall space complexity is O(N) in the worst case and O(log N) in the average case.
