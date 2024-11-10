class Solution:
    def pruneTree(self, root):
        # Base case: if the current node is None, return None
        if not root:
            return None

        # Recursively prune the left and right subtrees
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # If the current node is a leaf (no children) and its value is 0, prune it (return None)
        if not root.left and not root.right and root.val == 0:
            return None

        # Return the node itself if it's not pruned
        return root

# Time Complexity (TC): O(N)
# - The function visits each node once, performing a constant amount of work per node 
#   (checking and pruning conditions), resulting in O(N) time complexity, where N is 
#   the number of nodes in the tree.

# Space Complexity (SC): O(H)
# - The space complexity is O(H), where H is the height of the tree, due to the recursive 
#   call stack. 
# - In the worst case (e.g., a completely unbalanced tree), H could be O(N), making the 
#   space complexity O(N).
# - In the best case (a balanced tree), H is O(log N), so the space complexity would be 
#   O(log N).
