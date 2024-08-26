"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def solve(node):
            if not node:
                return
            for n in node.children:
                solve(n)
            res.append(node.val)
        
        solve(root)
        return res
