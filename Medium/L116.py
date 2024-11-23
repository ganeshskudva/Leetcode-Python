"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Connects each node to its next right node in a perfect binary tree.
        If there is no next right node, the 'next' pointer should be set to None.
        """
        # If the root is None (i.e., the tree is empty), return None.
        if not root:
            return root
        
        # Initialize a deque (double-ended queue) to perform level-order traversal (BFS).
        # Start with the root node in the queue.
        q = deque([root])
        
        # While there are nodes to process in the queue:
        while q:
            # Determine the size of the current level (number of nodes in this level).
            sz = len(q)
            
            # Loop through all nodes in the current level.
            for idx in range(sz):
                # Pop the first node from the left of the queue (this is the current node being processed).
                curr = q.popleft()
                
                # If this is not the last node in the current level,
                # set the 'next' pointer of the current node to point to the next node in the queue.
                if idx != sz - 1:
                    curr.next = q[0]  # Set the 'next' pointer to the next node in the queue.
                
                # If the current node has a left child, add it to the queue for the next level.
                if curr.left:
                    q.append(curr.left)
                
                # If the current node has a right child, add it to the queue for the next level.
                if curr.right:
                    q.append(curr.right)
        
        # After processing all levels, return the root of the tree (with 'next' pointers correctly set).
        return root

# Time Complexity (TC):
# O(n) - Each node in the tree is visited exactly once during the level-order traversal,
# where 'n' is the total number of nodes in the tree.

# Space Complexity (SC):
# O(w) - The maximum width of the tree determines the maximum size of the queue.
# In a perfect binary tree, the maximum width occurs at the last level, where there are n/2 nodes.
# Thus, the space complexity is O(n) in the worst case.

