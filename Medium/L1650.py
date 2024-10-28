"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

## iterative
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q  # Initialize two pointers, starting at nodes p and q

        # Traverse upwards until both pointers are equal
        while a != b:
            # Move pointer 'a' to its parent, or reset to 'q' if 'a' reaches the root (None)
            a = q if not a else a.parent
            
            # Move pointer 'b' to its parent, or reset to 'p' if 'b' reaches the root (None)
            b = p if not b else b.parent

        # Both pointers will eventually meet at the lowest common ancestor, return it
        return a

# Time Complexity (TC): O(h), where h is the height of the tree.
# - Each pointer traverses up to the root, covering a maximum of h steps. 
# - If they don’t meet on the first pass, they meet on the second, totaling O(h) steps.

# Space Complexity (SC): O(1)
# - Only two pointers (`a` and `b`) are used for traversal, making it a constant space solution.

## recrusive
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Set to keep track of ancestors of node p
        ancestors = set()

        # Helper function to find the path from a node up to the root
        def find_path_to_root(node, visited):
            if not node:
                return None
            # If we've already visited this node, return it as it could be the LCA
            if node in visited:
                return node
            # Add the current node to visited ancestors set
            visited.add(node)
            # Recur upwards to the parent
            return find_path_to_root(node.parent, visited)

        # Traverse upwards from `p`, marking all ancestors in the set
        find_path_to_root(p, ancestors)
        # Traverse upwards from `q`, checking each ancestor in `p`'s path
        return find_path_to_root(q, ancestors)

# Time Complexity (TC): O(h), where h is the height of the tree.
# - Each node (p and q) is traversed up to the root, covering up to h levels.

# Space Complexity (SC): O(h)
# - The recursion stack and the `ancestors` set both use space proportional to the height of the tree.
# - `ancestors` may store up to h nodes in the worst case, and the recursive call stack can go as deep as h.
