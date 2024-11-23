# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        """
        Find the nearest right node to the given node `u` in a binary tree.
        
        :param root: The root of the binary tree.
        :param u: The target node.
        :return: The nearest right node on the same level as `u`, or None if no such node exists.
        """
        # Edge case: if the root is None, return None
        if not root:
            return None
        
        # Initialize a queue for level-order traversal
        q = deque([root])

        # Perform level-order traversal
        while q:
            sz = len(q)  # Number of nodes at the current level
            for idx in range(sz):
                node = q.popleft()  # Process the next node in the queue
                
                # Check if this is the target node
                if node == u:
                    # If it's the last node in the level, return None
                    # Otherwise, return the next node in the queue (same level)
                    return None if idx == sz - 1 else q[0]
                
                # Add the left and right children to the queue if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        # If the target node is not found, return None
        return None

# Time Complexity (TC):
# O(n) - Each node in the binary tree is visited exactly once during the traversal.

# Space Complexity (SC):
# O(w) - The maximum width of the tree determines the maximum size of the queue,
# where `w` is the largest number of nodes in any level of the tree.
