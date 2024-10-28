from collections import defaultdict, deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Return an empty list if the tree is empty

        # Dictionary to store nodes by their column index
        mp = defaultdict(list)
        
        # Queue for BFS traversal, storing pairs of (node, column index)
        q = deque([(root, 0)])

        # Perform BFS to populate the column-wise node map
        while q:
            node, col = q.popleft()  # Get the current node and its column index
            mp[col].append(node.val)  # Append node value to its respective column in mp
            
            # If there's a left child, add it to the queue with column index -1
            if node.left:
                q.append((node.left, col - 1))
            
            # If there's a right child, add it to the queue with column index +1
            if node.right:
                q.append((node.right, col + 1))

        # Collect results from mp, sorted by column index
        return [mp[k] for k in sorted(mp)]

# Time Complexity (TC): O(n log k), where `n` is the number of nodes and `k` is the number of unique columns.
# - Traversing all nodes with BFS takes O(n).
# - Sorting the column indices takes O(k log k), where `k` is the number of unique columns.

# Space Complexity (SC): O(n)
# - The dictionary `mp` stores each node value, requiring O(n) space.
# - The queue `q` for BFS can hold up to O(n) nodes in the worst case, especially in a complete binary tree.
# - Thus, the overall space complexity is O(n).
