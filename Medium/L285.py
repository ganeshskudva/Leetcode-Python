# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inorderSuccessor(self, root, p):
    succ = None  # Initialize successor as None
    
    # Traverse the tree iteratively
    while root:
        if p.val < root.val:  # If 'p' is less than the current node
            succ = root  # Current node is a potential successor
            root = root.left  # Move to the left subtree to check for a closer successor
        else:  # If 'p' is greater than or equal to the current node
            root = root.right  # Move to the right subtree
    
    return succ  # Return the last recorded successor

# Time Complexity (TC):
# - The function traverses the tree along its height.
# - In the worst case (for a skewed tree), the traversal goes through O(H), where H is the height of the tree.
# - For a balanced BST, the height is O(log N), and for a skewed tree, it is O(N).
# - Total TC: O(H), where H is the height of the tree.

# Space Complexity (SC):
# - The function uses constant space, as it employs an iterative approach with no recursion or additional data structures.
# - Total SC: O(1).
