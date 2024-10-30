# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the current node is None, return None
        if not root:
            return None

        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root node of the inverted tree
        return root

# Time Complexity (TC):
# - The function visits each node exactly once, and each visit involves constant-time operations (swapping and recursive calls).
# - Therefore, the time complexity is O(N), where N is the total number of nodes in the tree.

# Space Complexity (SC):
# - The space complexity is determined by the recursion stack.
# - In the worst case (for a skewed tree), the recursion depth can be O(N).
# - In the best/average case (for a balanced tree), the recursion depth is O(log N).
# - Thus, the space complexity is O(N) in the worst case and O(log N) in the average case.

# bfs
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the root is None, there's nothing to invert
        if not root:
            return root

        # Initialize a queue with the root node for level-order traversal
        q = deque([root])

        # Perform level-order traversal to invert each subtree
        while q:
            # Pop the current node from the queue
            node = q.popleft()
            
            # Swap the left and right children of the current node
            node.left, node.right = node.right, node.left

            # Add left and right children to the queue if they exist
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        # Return the root of the inverted tree
        return root

# Time Complexity (TC):
# - The function visits each node exactly once, performing constant-time operations (swapping and queue operations).
# - Therefore, the time complexity is O(N), where N is the total number of nodes in the tree.

# Space Complexity (SC):
# - The space complexity depends on the queue, which stores nodes at each level.
# - In the worst case (for a balanced binary tree), the maximum number of nodes in the queue is the width of the tree, which can be O(N/2) = O(N).
# - Therefore, the space complexity is O(N) in the worst case.

