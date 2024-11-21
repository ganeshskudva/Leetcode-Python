# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Helper function to recursively check if a path sum equals the target
        def solve(node, tgt=0):
            # Base case: if the node is None, return False
            if not node:
                return False
            # Check if the current node is a leaf and its value equals the remaining target
            if tgt == node.val and not node.left and not node.right:
                return True
            # Recur on the left and right subtrees with the updated target
            return solve(node.left, tgt - node.val) or solve(node.right, tgt - node.val)

        # Start the recursion with the root and the target sum
        return solve(root, targetSum)

# Time Complexity (TC): O(n)
# - Each node is visited once in the worst case, where n is the number of nodes in the tree.
# - The function makes a constant amount of work per node (comparison and subtraction).
# Total: O(n).

# Space Complexity (SC): O(h)
# - The recursive call stack can go as deep as the height of the tree (h).
# - In the worst case of a skewed tree, h = n, making the space complexity O(n).
# - In the best case of a balanced tree, h = log(n), making the space complexity O(log(n)).
# Total: O(h), where h is the height of the tree.

# iterative
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # Use a stack for DFS, storing (node, current_sum)
        stack = [(root, targetSum - root.val)]
        
        while stack:
            node, curr_sum = stack.pop()
            
            # If it's a leaf node and the remaining sum is 0, return True
            if not node.left and not node.right and curr_sum == 0:
                return True
            
            # Add the right and left children to the stack with updated remaining sum
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
        
        return False

# Time Complexity (TC): O(n)
# - Each node is visited exactly once, where n is the number of nodes in the tree.
# - The iterative approach does not change the time complexity.

# Space Complexity (SC): O(h)
# - The explicit stack can hold up to h elements in the worst case.
# - In the best case of a balanced tree, h = log(n).
# - In the worst case of a skewed tree, h = n.
