class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        
        # Dictionary to store the mapping from original nodes to their copies
        mp = {}
        
        def solve(node):
            if not node:
                return None
            # If the node is already copied, return the copy
            if node in mp:
                return mp[node]
            
            # Create a copy of the current node
            copy_node = NodeCopy(node.val)
            mp[node] = copy_node
            
            # Recursively copy the left, right, and random pointers
            copy_node.left = solve(node.left)
            copy_node.right = solve(node.right)
            copy_node.random = solve(node.random)
            
            return copy_node
        
        # Start the copying process from the root
        return solve(root)

# Time Complexity (TC):
# - Each node in the tree is visited exactly once.
# - The operations performed for each node (copying the node, accessing the dictionary, and assigning pointers) are O(1).
# - Thus, the overall time complexity is O(n), where n is the number of nodes in the tree.

# Space Complexity (SC):
# - The dictionary `mp` stores mappings for all nodes in the original tree, requiring O(n) space.
# - The recursion stack can go as deep as the height of the tree. In the worst case of a skewed tree, the recursion depth is O(n). In the best case (a balanced tree), the depth is O(log n).
# - Therefore, the total space complexity is O(n), dominated by the dictionary storage. 
