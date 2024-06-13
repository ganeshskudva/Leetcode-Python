# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, q = [], deque()
        if not root:
            return res
        q.append(root)

        while q:
            size, tmp = len(q), []
            for _ in range(size):
                n = q.popleft()
                tmp.append(n.val)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(tmp)

        return res
