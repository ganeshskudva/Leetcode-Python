from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Initialize a queue with the root node for level-order traversal
        # Time Complexity: O(1) for initialization
        # Space Complexity: O(1) for storing `q` and `left_most`
        q = deque([root])
        left_most = None  # To store the leftmost node of the current level
        
        # Perform a breadth-first traversal
        # Time Complexity: O(n), where n is the number of nodes in the tree
        # Each node is enqueued and dequeued exactly once.
        while q:
            # Get the size of the current level
            sz = len(q)
            # Set `left_most` to the first node in this level (leftmost node)
            left_most = q[0]
            
            # Process each node in the current level
            # Time Complexity per level: O(level size), so overall for all levels: O(n)
            for _ in range(sz):
                # Pop the current node from the queue
                node = q.popleft()
                
                # Append the left child to the queue if it exists
                # Space Complexity: O(n), total queue space can reach all nodes in the bottom level
                if node.left:
                    q.append(node.left)
                
                # Append the right child to the queue if it exists
                if node.right:
                    q.append(node.right)
        
        # After the loop, `left_most` will contain the leftmost node of the bottom row
        return left_most.val

# Overall Complexity Summary:
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
#                  We perform a level-order traversal, visiting each node once.
# Space Complexity: O(n), where n is the number of nodes in the binary tree.
#                  The queue can hold up to n/2 nodes in the last level in the worst case.
