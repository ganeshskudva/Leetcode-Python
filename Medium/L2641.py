# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If the root is None, return None
        if not root:
            return root
        
        # Set the root's value to 0
        root.val = 0
        
        # Queue for level-order traversal (BFS)
        q = deque([root])
        
        # Perform level-order traversal
        while q:
            size, tot, tmp = len(q), 0, []  # size is the number of nodes in the current level
            for _ in range(size):
                node = q.popleft()  # Pop the node from the front of the queue
                tmp.append(node)  # Add the node to a temporary list
                
                # If the node has a left child, add it to the queue and accumulate its value
                if node.left:
                    q.append(node.left)
                    tot += node.left.val  # Accumulate the sum of values for this level
                
                # If the node has a right child, add it to the queue and accumulate its value
                if node.right:
                    q.append(node.right)
                    tot += node.right.val  # Accumulate the sum of values for this level
            
            # Now that we know the total sum for the current level, update the node values
            for node in tmp:
                tot_sum = tot  # Start with the total sum
                # Subtract the left child's value from the total if it exists
                if node.left:
                    tot_sum -= node.left.val
                # Subtract the right child's value from the total if it exists
                if node.right:
                    tot_sum -= node.right.val
                # Update the left child's value
                if node.left:
                    node.left.val = tot_sum
                # Update the right child's value
                if node.right:
                    node.right.val = tot_sum
        
        # Return the modified root
        return root

# Time Complexity (TC):
# - The solution performs a level-order traversal (BFS) of the tree, where each node is processed once.
# - For each level, we calculate the total sum of the node values (O(N) where N is the number of nodes) and then update the node values (O(N)).
# - Therefore, the total time complexity is O(N), where N is the total number of nodes in the tree.

# Space Complexity (SC):
# - The space complexity is determined by the maximum number of nodes held in the queue during the level-order traversal.
# - In the worst case, the queue can hold O(W) nodes, where W is the maximum width of the tree. In a full binary tree, W can be as large as N/2.
# - The temporary list `tmp` also holds O(W) nodes at a time, but this doesn't increase the overall complexity.
# - Therefore, the total space complexity is O(W), where W is the maximum width of the tree (in the worst case O(N/2)).

