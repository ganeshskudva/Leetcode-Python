# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize a queue for BFS and the result list.
        q, res = deque([root]), []
        
        # If the tree is empty, return an empty list.
        if not root:
            return res
        
        # Boolean to toggle traversal direction.
        left = True

        # Perform level-order traversal.
        while q:
            size, tmp = len(q), []  # Track current level size and temporary storage.
            
            # Process all nodes at the current level.
            for _ in range(size):
                n = q.popleft()  # Pop the node from the queue.
                tmp.append(n.val)  # Add the node's value to the current level.
                
                # Add children to the queue for the next level.
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            
            # Append current level values to result, reversing if needed.
            res.append(tmp) if left else res.append(tmp[::-1])
            
            # Toggle the direction for the next level.
            left = not left
        
        # Return the final zigzag level order traversal.
        return res

# Time Complexity (TC): O(n)
# - Each node is visited exactly once during traversal.

# Space Complexity (SC): O(n)
# - The queue (deque) may hold up to `n/2` nodes at the deepest level in the worst case.
