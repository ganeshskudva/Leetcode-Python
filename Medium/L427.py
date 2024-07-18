"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def solve(x1, x2, y1, y2):
            if x1 == x2:
                val = True if grid[x1][y1] == 1 else False
                return Node(val, TreeNode, None, None, None, None)

            rowMid = (x1 + x2) // 2
            colMid = (y1 + y2) // 2
            topLeft = solve(x1, rowMid, y1, colMid)
            topRight = solve(x1, rowMid, colMid + 1, y2)
            bottomLeft = solve(rowMid + 1, x2, y1, colMid)
            bottomRight = solve(rowMid + 1, x2, colMid + 1, y2)

            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topRight.val == topLeft.val and topRight.val == bottomLeft.val and topRight.val == bottomRight.val:
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return solve(0, len(grid) - 1, 0, len(grid[0]) - 1)
