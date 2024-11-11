# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # Stack to simulate in-order traversal, storing nodes to be processed
        self.stack = []
        # Initialize by pushing all left children of the root onto the stack
        self._leftmost_inorder(root)
        # Time Complexity (TC) for __init__: O(h), where h is the height of the tree.
        # Space Complexity (SC): O(h), since we store at most h nodes on the stack at any given time.

    def _leftmost_inorder(self, node):
        # Push all nodes from the current node down to the leftmost leaf
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the topmost node, which is the next smallest element
        topmost_node = self.stack.pop()
        
        # If there is a right child, we push all its left children onto the stack
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        
        # Return the value of the topmost node
        return topmost_node.val
        # Time Complexity (TC) for next: Amortized O(1), as each node is visited once.
        # Space Complexity (SC): O(h), where h is the height of the tree due to the stack usage.

    def hasNext(self) -> bool:
        # Return True if there are nodes left in the stack
        return len(self.stack) > 0
        # Time Complexity (TC) for hasNext: O(1), as it only checks the stack's length.
        # Space Complexity (SC): O(1), no additional space required.
