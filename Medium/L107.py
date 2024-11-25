from collections import deque
from typing import Optional, List

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform a bottom-up level order traversal of a binary tree.

        Args:
        root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        List[List[int]]: A list of levels, each containing node values, from bottom to top.

        Time Complexity: O(n), where n is the number of nodes in the binary tree.
            - Each node is visited exactly once.
        Space Complexity: O(n), for the queue and result list, as they can store up to n nodes.
        """
        res = []  # Final result list
        if not root:  # If the tree is empty, return an empty list
            return res

        q = deque([root])  # Initialize a queue with the root node
        while q:
            sz = len(q)  # Number of nodes at the current level
            tmp = []  # Temporary list to store values at the current level
            
            # Process all nodes at the current level
            for _ in range(sz):
                node = q.popleft()  # Remove the front node from the queue
                tmp.append(node.val)  # Add its value to the temporary list

                # Add child nodes to the queue if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(tmp)  # Append the current level to the result list

        return res[::-1]  # Reverse the result list to achieve bottom-up order

# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), due to the queue and result list that can store up to n nodes.
