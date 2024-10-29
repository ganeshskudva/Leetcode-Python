# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize result list and queue for level-order traversal
        res, q = [], deque([root])

        # Edge case: if root is None, return an empty list
        if not root:
            return res

        # Perform a level-order traversal of the tree
        while q:
            size = len(q)  # Number of nodes at the current level
            # Append the last node's value at the current level (rightmost node)
            res.append(q[-1].val)
            # Traverse each node at the current level
            for _ in range(size):
                n = q.popleft()  # Pop the leftmost node in the queue
                # Add left and right children to the queue for the next level
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return res

# Time Complexity (TC):
# - The time complexity is O(N), where N is the number of nodes in the tree.
# - Each node is visited once in a level-order traversal.

# Space Complexity (SC):
# - The space complexity is O(D), where D is the maximum number of nodes at any level in the tree (the tree's maximum width).
# - In the worst case, this can be O(N) if the tree is complete or very wide.
# - Additionally, the result list `res` stores the rightmost node value from each level, which can take up to O(H) space, where H is the height of the tree.
# - Overall, the space complexity is O(N) in the worst case due to the queue and result storage requirements.

