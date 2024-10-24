# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base case: if either of the trees is null, they are flip equivalent 
        # if both are null, otherwise they are not.
        if not root1 or not root2:
            return not root1 and not root2
        
        # If the values of the two root nodes are not the same, 
        # the trees are not flip equivalent.
        if root1.val != root2.val:
            return False
        
        # Recursively check for two cases:
        # 1. Check if the left subtree of root1 is flip equivalent to the left subtree of root2
        #    AND the right subtree of root1 is flip equivalent to the right subtree of root2.
        # 2. Check if the left subtree of root1 is flip equivalent to the right subtree of root2
        #    AND the right subtree of root1 is flip equivalent to the left subtree of root2.
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) 
                or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))

# Time Complexity (TC):
# Each node in the tree is visited once in the recursive process, and for each node, 
# a constant amount of work is done (comparing values and making recursive calls). 
# Therefore, the time complexity is O(n), where n is the total number of nodes in the tree.
# In the worst case, both trees have n nodes.

# Space Complexity (SC):
# The space complexity is primarily determined by the recursion depth, which in the worst case 
# can be the height of the tree. The height of a balanced binary tree is O(log n), while in the 
# worst case (skewed tree), the height can be O(n). Therefore, the space complexity is O(h), 
# where h is the height of the tree, leading to O(n) in the worst case.
