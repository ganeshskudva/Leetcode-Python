# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def solve(start, end):
            res = []
            if start > end:
                res.append(None)
                return res
            
            for i in range(start, end + 1):
                left_sub_trees, right_sub_trees = solve(start, i - 1), solve(i + 1, end)
                
                for left in left_sub_trees:
                    for right in right_sub_trees:
                        root = TreeNode(i)
                        root.left, root.right = left, right
                        res.append(root)
            
            return res
        
        return solve(1, n)
