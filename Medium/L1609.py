class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q, lvl = deque([root]), 0

        while q:
            sz = len(q)
            # Set constraints based on level type (even/odd)
            is_even_level = lvl % 2 == 0
            prev_val = float('-inf') if is_even_level else float('inf')

            for _ in range(sz):
                node = q.popleft()

                # Check if node's value satisfies even/odd level conditions
                if (node.val % 2 == 0 and is_even_level) or (node.val % 2 != 0 and not is_even_level):
                    return False

                # Check order based on level type
                if (is_even_level and node.val <= prev_val) or (not is_even_level and node.val >= prev_val):
                    return False

                # Update the previous node's value for order comparison
                prev_val = node.val

                # Add children to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Move to the next level
            lvl += 1

        return True

# Space Complexity (SC): O(N)
# - The space complexity is O(N) because in the worst case, the queue holds all nodes in the last level, 
#   which could be up to N/2 nodes, where N is the total number of nodes in the tree.

# Time Complexity (TC): O(N)
# - The time complexity is O(N) because each node is processed once during the level-order traversal. 
#   Each level has a fixed number of operations based on the nodes in that level, resulting in O(N) operations for N nodes.
