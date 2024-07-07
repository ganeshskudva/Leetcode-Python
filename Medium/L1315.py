# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.tot = 0
        if not root: return self.root

        def is_even(n):
            return n.val % 2 == 0

        def solve(node, parent=None, grand_parent=None):
            if not node: return

            if grand_parent and is_even(grand_parent):
                self.tot += node.val

            solve(node.left, node, parent)
            solve(node.right, node, parent)

        solve(root)
        return self.tot
