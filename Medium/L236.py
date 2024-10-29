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
