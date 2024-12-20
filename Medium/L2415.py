# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        queue = deque([root])
        level = 0

        while queue:
            size = len(queue)
            # Store current level nodes
            if level % 2 == 1:
                values = [node.val for node in queue]
                # Reverse values and assign them back
                for i in range(size):
                    queue[i].val = values[size - 1 - i]

            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return root

# Time Complexity (TC):
# O(n) - Each node is visited once, and reversing values at odd levels involves iterating over all nodes at that level.
# Space Complexity (SC):
# O(n) - Maximum space required for the queue is proportional to the width of the binary tree (maximum number of nodes at any level).