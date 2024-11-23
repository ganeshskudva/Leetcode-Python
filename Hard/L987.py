from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform vertical order traversal of a binary tree using BFS.

        :param root: Root node of the binary tree.
        :return: A list of lists where each inner list contains the vertical order traversal of nodes.
        """
        if not root:
            return []

        # Dictionary to store nodes: {x-coordinate: {y-coordinate: [node values]}}
        nodes_map = defaultdict(lambda: defaultdict(list))

        # Queue for BFS: stores tuples of (node, x-coordinate, y-coordinate)
        queue = deque([(root, 0, 0)])

        # Perform BFS
        while queue:
            node, x, y = queue.popleft()

            # Add the node value to the corresponding (x, y) position
            nodes_map[x][y].append(node.val)

            # Add left child to the queue with updated coordinates
            if node.left:
                queue.append((node.left, x - 1, y + 1))

            # Add right child to the queue with updated coordinates
            if node.right:
                queue.append((node.right, x + 1, y + 1))

        # Result list for final sorted order
        result = []

        # Sort by x-coordinate, then by y-coordinate, and finally by node values
        for x in sorted(nodes_map.keys()):  # Sort by x-coordinate
            column = []
            for y in sorted(nodes_map[x].keys()):  # Sort by y-coordinate
                column.extend(sorted(nodes_map[x][y]))  # Sort values within the same (x, y)
            result.append(column)

        return result

# Time Complexity (TC):
# O(n log n) - BFS visits each node once (O(n)), but sorting the x-coordinates and y-coordinates dominates the complexity.
# Sorting within a single (x, y) bucket involves sorting small arrays.

# Space Complexity (SC):
# O(n) - The `nodes_map` dictionary and the BFS queue together use space proportional to the number of nodes.
