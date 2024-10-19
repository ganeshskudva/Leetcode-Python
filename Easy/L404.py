class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # If the root is None, there are no leaves, so return 0
        if not root:
            return 0
        
        # Helper function to check if a node is a leaf (i.e., no left or right children)
        def is_leaf(node):
            return node and not node.left and not node.right
        
        # Initialize a queue for level-order traversal, starting with the root node and a flag (False means it's not a left child)
        q, tot = deque([(root, False)]), 0
        
        # Perform level-order traversal
        while q:
            # Dequeue the current node and whether it is a left child
            node, is_left = q.popleft()
            
            # If the current node is a leaf and it is a left child, add its value to the total sum
            if is_leaf(node) and is_left:
                tot += node.val
            
            # If the node has a left child, add it to the queue and mark it as a left child
            if node.left:
                q.append((node.left, True))
            # If the node has a right child, add it to the queue and mark it as a right child
            if node.right:
                q.append((node.right, False))
        
        # Return the total sum of the left leaves
        return tot

# Time Complexity (TC):
# The time complexity is O(n), where `n` is the number of nodes in the binary tree.
# We visit each node exactly once during the level-order traversal, so the time complexity is linear.

# Space Complexity (SC):
# The space complexity is O(n), where `n` is the number of nodes in the binary tree.
# In the worst case, the queue may hold up to O(n) nodes (especially in a full binary tree, where the last level may contain n/2 nodes).
# Therefore, the space complexity is proportional to the number of nodes in the tree.
