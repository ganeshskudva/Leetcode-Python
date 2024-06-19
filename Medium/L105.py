# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return 
        
        mp = defaultdict(int)
        for i in range(len(inorder)):
            mp[inorder[i]] = i
        
        def solve(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return 
            
            root = TreeNode(preorder[pre_start])
            in_root = mp[root.val]
            num_left = in_root - in_start

            root.left = solve(pre_start + 1, pre_start + num_left, in_start, in_root - 1)
            root.right = solve(pre_start + num_left + 1, pre_end, in_root + 1, in_end)
            
            return root
        
            
        return solve(0, len(preorder) - 1, 0, len(inorder) - 1) 
