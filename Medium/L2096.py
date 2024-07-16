# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def get_lca(node, start, dest):
            if not node:
                return
            if node.val == start or node.val == dest:
                return node

            left, right = get_lca(node.left, start, dest), get_lca(node.right, start, dest)
            if left and right:
                return node

            return left if left else right

        def traverse(node, val, path=None):
            if path is None:
                path = []
            if not node:
                return False
            if node.val == val:
                return True

            path.append('L')
            if traverse(node.left, val, path):
                return True
            del path[-1]

            path.append('R')
            if traverse(node.right, val, path):
                return True
            del path[-1]

            return False

        lca = get_lca(root, startValue, destValue)
        lca_to_start, lca_to_dest = [], []

        traverse(lca, startValue, lca_to_start)
        traverse(lca, destValue, lca_to_dest)

        res = []
        for _ in range(len(lca_to_start)):
            res.append('U')
        res.extend(lca_to_dest)
        return ''.join(res)
