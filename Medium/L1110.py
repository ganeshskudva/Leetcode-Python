# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        del_set, res = set(to_delete), []
        
        def solve(node, is_root):
            if not node:
                return None
            deleted = node.val in del_set
            if is_root and not deleted:
                res.append(node)
            node.left, node.right = solve(node.left, deleted), solve(node.right, deleted)
            
            return node if not deleted else None
        
        solve(root, True)
        return res
