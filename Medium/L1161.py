from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Initialize level counter and queue for level-order traversal
        lvl, q = 0, deque([root])  # Start at level 0 with root node
        mx, mx_lvl = float('-inf'), 0  # Track max sum and level with max sum

        while q:
            sz, tot = len(q), 0  # Number of nodes at current level, level sum
            for _ in range(sz):  # Traverse all nodes at current level
                node = q.popleft()
                tot += node.val  # Accumulate node values for the level

                if node.left:  # Add left child to queue if it exists
                    q.append(node.left)
                if node.right:  # Add right child to queue if it exists
                    q.append(node.right)
            lvl += 1  # Increment level
            if tot > mx:  # Update max sum and its corresponding level if needed
                mx, mx_lvl = tot, lvl

        return mx_lvl

# Time Complexity (TC):
# O(n) - Each node is visited exactly once during the level-order traversal.

# Space Complexity (SC):
# O(w) - Maximum width of the tree determines the space used by the queue, 
# where 'w' is the largest number of nodes at any level of the tree.
