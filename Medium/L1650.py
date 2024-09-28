"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Initialize two pointers, 'a' starting at node p and 'b' starting at node q
        a, b = p, q
        
        # Traverse upwards until both pointers are equal
        while a != b:
            # Move pointer 'a' to its parent, or reset to q if 'a' reaches the root (None)
            a = q if not a else a.parent
            
            # Move pointer 'b' to its parent, or reset to p if 'b' reaches the root (None)
            b = p if not b else b.parent
        
        # Both pointers will eventually meet at the lowest common ancestor, return it
        return a
