# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def solve(node, tgt=0, tmp=[]):
            if not node:
                return
            tmp.append(node.val)
            if tgt == node.val and not node.left and not node.right:
                res.append(list(tmp))
            solve(node.left, tgt - node.val, tmp)
            solve(node.right, tgt - node.val, tmp)
            del tmp[-1]

        solve(root, targetSum)
        return res
