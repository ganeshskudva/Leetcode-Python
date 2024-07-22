# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.val = 0
        q = deque([root])
        
        while q:
            size, tot, tmp = len(q), 0, []
            for _ in range(size):
                node = q.popleft()
                tmp.append(node)
                
                if node.left:
                    q.append(node.left)
                    tot += node.left.val
                
                if node.right:
                    q.append(node.right)
                    tot += node.right.val
            for node in tmp:
                tot_sum = tot
                if node.left:
                    tot_sum -= node.left.val
                if node.right:
                    tot_sum -= node.right.val
                if node.left:
                    node.left.val = tot_sum
                if node.right:
                    node.right.val = tot_sum
            
        return root
