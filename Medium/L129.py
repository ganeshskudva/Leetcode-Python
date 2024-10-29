## recursive
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Helper function to perform DFS and calculate path sums
        def dfs(node, curr_sum):
            # Base case: if the node is None, it contributes nothing to the sum
            if not node:
                return 0

            # Update the current sum by moving the digit left and adding the node's value
            curr_sum = curr_sum * 10 + node.val
            
            # If it's a leaf node, return the current path sum
            if not node.left and not node.right:
                return curr_sum
            
            # Recursively calculate the sum from left and right subtrees and return their total
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)

        # Start the DFS from the root with an initial sum of 0
        return dfs(root, 0)

# Time Complexity (TC): O(n), where n is the number of nodes in the tree.
# - Each node is visited once in the DFS traversal, so the time complexity is O(n).

# Space Complexity (SC): O(h), where h is the height of the tree.
# - The recursion stack can go as deep as the height of the tree, leading to O(h) space complexity.
# - In the worst case, h could be O(n) if the tree is completely unbalanced (like a linked list),
#   but it is O(log n) for a balanced tree.


## iterative DFS
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total_sum = 0
        stack = [(root, 0)]  # Stack contains pairs of (node, current_path_sum)

        # Iterative DFS using a stack
        while stack:
            node, curr_sum = stack.pop()
            # Update the current path sum
            curr_sum = curr_sum * 10 + node.val
            
            # Check if it is a leaf node
            if not node.left and not node.right:
                total_sum += curr_sum  # Add the leaf path sum to the total
            else:
                # Push children onto the stack with updated path sums
                if node.right:
                    stack.append((node.right, curr_sum))
                if node.left:
                    stack.append((node.left, curr_sum))
        
        return total_sum

# Time Complexity (TC): O(n), where n is the number of nodes in the tree.
# - Each node is visited exactly once in the DFS traversal, making the time complexity O(n).

# Space Complexity (SC): O(h), where h is the height of the tree.
# - The stack holds up to h elements in the case of a skewed tree (worst case),
#   which is O(h) space complexity.
# - In a balanced tree, h is approximately log(n), making it O(log n).
