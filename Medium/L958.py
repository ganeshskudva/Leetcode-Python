from typing import Optional
from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Initialize end flag to track if we've seen a missing node in the tree
        end = False
        # Use a queue to perform level-order traversal, starting with the root
        q = deque([root])

        while q:
            # Get the current node from the front of the queue
            curr = q.popleft()

            # If the current node is None, mark that we have encountered an empty spot
            if not curr:
                end = True
            else:
                # If we've previously seen a None (end is True) and encounter a non-None node,
                # it means the tree is not complete
                if end:
                    return False
                # Enqueue the left and right children to continue level-order traversal
                q.append(curr.left)
                q.append(curr.right)

        # If we've traversed the entire tree without finding a misplaced node, it's complete
        return True

# Time Complexity (TC):
# - We perform a level-order traversal of the tree, visiting each node exactly once.
# - Therefore, the time complexity is O(N), where N is the number of nodes in the tree.

# Space Complexity (SC):
# - The space complexity is O(W), where W is the maximum width of the tree.
# - In the worst case, W can be O(N) if the tree is completely unbalanced or a complete binary tree at its widest level.
# - However, typically for a balanced tree, the space complexity is O(N/2), which simplifies to O(N).
