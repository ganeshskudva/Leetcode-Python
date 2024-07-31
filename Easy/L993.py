# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        q.append((0, -1, root))
        x_parent, x_lvl, y_parent, y_lvl = None, 0, None, 0
        lvl = 0

        while q:
            size = len(q)
            lvl += 1
            for _ in range(size):
                (level, parent, node) = q.popleft()

                if node.val == x:
                    x_parent, x_lvl = parent, level
                if node.val == y:
                    y_parent, y_lvl = parent, level

                if node.left:
                    q.append((lvl, node.val, node.left))

                if node.right:
                    q.append((lvl, node.val, node.right))

        return x_parent != y_parent and x_lvl == y_lvl


# DFS
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []

        def solve(node, parent=None, depth=0):
            if not node:
                return
            if node.val == x or node.val == y:
                res.append((node.val, parent, depth))
            solve(node.left, node, depth + 1)
            solve(node.right, node, depth + 1)

        solve(root)
        return res[0][1] != res[1][1] and res[0][2] == res[1][2]
