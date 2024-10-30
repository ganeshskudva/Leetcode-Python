# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If both p and q are less than root, LCA must be in the left subtree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If both p and q are greater than root, LCA must be in the right subtree
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If neither of the above conditions is true, root is the LCA
        else:
            return root

# Time Complexity (TC): O(h), where h is the height of the binary search tree.
# In the average case for a balanced BST, this is O(log n), but in the worst case (skewed tree), it can be O(n),
# where n is the number of nodes.

# Space Complexity (SC): O(h) due to the recursion stack.
# In the average case, this is O(log n) for a balanced tree, and O(n) in the worst case for a skewed tree.

