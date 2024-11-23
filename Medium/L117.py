"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Using deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Connects each node in a perfect binary tree to its next right node.
        If there is no next right node, the 'next' pointer should be set to None.
        """
        # If the root is None, return None as there is no tree to process.
        if not root:
            return root
        
        # Initialize a queue for level-order traversal (BFS), starting with the root node.
        q = deque([root])
        
        # Perform level-order traversal.
        while q:
            # Determine the number of nodes at the current level.
            sz = len(q)
            
            # Traverse all nodes at the current level.
            for i in range(sz):
                # Remove the front node from the queue.
                node = q.popleft()
                
                # If this is not the last node of the current level,
                # set its 'next' pointer to the next node in the queue.
                if i != sz - 1:
                    node.next = q[0]
                
                # Add the left child to the queue if it exists.
                if node.left:
                    q.append(node.left)
                
                # Add the right child to the queue if it exists.
                if node.right:
                    q.append(node.right)
        
        # Return the modified root after setting all 'next' pointers.
        return root

# Time Complexity (TC):
# O(n) - Each node is visited exactly once during the level-order traversal,
# where 'n' is the total number of nodes in the tree.

# Space Complexity (SC):
# O(w) - The maximum width of the tree determines the maximum size of the queue.
# In a perfect binary tree, the maximum width occurs at the last level, where there are n/2 nodes.
# Thus, in the worst case, the space complexity is O(n).

# without using queue
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Connect each node to its next right node for a general binary tree.
        """
        if not root:
            return None
        
        # Start with the root node.
        current = root
        
        # Dummy node to track the start of the next level.
        dummy = Node(0)
        
        while current:
            # Tail tracks the current node in the next level being built.
            tail = dummy
            dummy.next = None  # Reset the dummy for the next level.

            # Traverse the current level using `next` pointers.
            while current:
                # If the current node has a left child, connect it to the tail.
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                # If the current node has a right child, connect it to the tail.
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                # Move to the next node in the current level using the `next` pointer.
                current = current.next
            
            # Move to the first node of the next level.
            current = dummy.next
        
        return root

# Time Complexity (TC):
# O(n) - Each node is visited exactly once during the traversal to establish its `next` pointer.

# Space Complexity (SC):
# O(1) - No additional space is used apart from a few pointers (`dummy` and `tail`). 
# The connections are established in-place, and no auxiliary data structures are used.

