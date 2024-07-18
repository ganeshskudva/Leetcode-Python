# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = [0] 
        
        def solve(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left, right = solve(node.left), solve(node.right)
            ret = []
            if left and right:
                for i in range(len(left)):
                    for j in range(len(right)):
                        if left[i] + right[j] <= distance:
                            res[0] += 1
            
            for i in range(len(left)):
                ret.append(left[i] + 1)
            for i in range(len(right)):
                ret.append(right[i] + 1)
            
            return ret
        
        solve(root)
        return res[0]
