from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        """
        Get all elements from two binary search trees in sorted order.
        
        :param root1: Root of the first binary search tree.
        :param root2: Root of the second binary search tree.
        :return: A list of all elements in sorted order.
        """
        res = []  # Final result list
        if not root1 and not root2:
            return res
        
        # Stack for iterative in-order traversal
        st1, st2 = [], []

        # Closure to push all left children of a subtree onto the stack
        def push_left(stack, node):
            while node:
                stack.append(node)
                node = node.left

        # Initialize the stacks with leftmost nodes of both trees
        push_left(st1, root1)
        push_left(st2, root2)

        # Merge elements from the two trees
        while st1 or st2:
            # Select the stack with the smaller current element
            if not st1:
                stack = st2
            elif not st2:
                stack = st1
            else:
                stack = st1 if st1[-1].val < st2[-1].val else st2

            # Pop the top element from the selected stack
            node = stack.pop()
            res.append(node.val)  # Add the node's value to the result

            # Push the leftmost nodes of the right subtree
            push_left(stack, node.right)

        return res

# Time Complexity (TC):
# O(m + n) - Each node from both trees is visited exactly once, where 'm' and 'n' are the number of nodes in root1 and root2, respectively.

# Space Complexity (SC):
# O(h1 + h2) - The stacks use space proportional to the height of the two trees, where 'h1' and 'h2' are the heights of root1 and root2.
