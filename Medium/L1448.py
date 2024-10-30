# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Initialize a counter to keep track of "good" nodes
        # Space Complexity: O(1) for storing an integer counter
        self.cnt = 0

        # Define a helper function to traverse the tree and count good nodes
        # Time Complexity of each call to `solve`: O(1)
        # Space Complexity per recursive call: O(h), where h is the height of the tree due to the call stack
        def solve(node, val=0):
            # Base case: if the node is None, return immediately
            if not node:
                return
            
            # If the node's value is greater than or equal to the max value seen so far (val), it is a "good" node
            if node.val >= val:
                self.cnt += 1  # Increment the count of good nodes
            
            # Recursive calls to the left and right children with the updated max value
            # Update val to the maximum of the current node's value and the current max value
            solve(node.left, max(node.val, val))
            solve(node.right, max(node.val, val))

        # Initial call to the solve function with the root's value as the starting max value
        solve(root, root.val)

        # Return the final count of good nodes
        return self.cnt

# Overall Complexity Summary:
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
#                  We visit each node exactly once in a depth-first traversal.
# Space Complexity: O(h), where h is the height of the binary tree.
#                   This is the maximum depth of the recursion stack.
#                   In the worst case (unbalanced tree), h = n, so the space complexity becomes O(n).
#                   In the best case (balanced tree), h = log(n), so the space complexity becomes O(log(n)).

