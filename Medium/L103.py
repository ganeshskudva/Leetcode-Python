# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, res = deque([root]), []
        if not root:
            return res
        
        left = True
        while q:
            size, tmp = len(q), []
            for _ in range(size):
                n = q.popleft()
                tmp.append(n.val)
                
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(tmp) if left else res.append(tmp[::-1])
            left = not left
        
        return res
