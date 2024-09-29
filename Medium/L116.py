class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
