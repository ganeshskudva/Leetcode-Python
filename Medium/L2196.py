# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map, child_map = {}, defaultdict(bool)

        for root, child, left in descriptions:
            if root not in node_map:
                node_map[root] = TreeNode(root)
            if child not in node_map:
                node_map[child] = TreeNode(child)
            if left:
                node_map[root].left = node_map[child]
            else:
                node_map[root].right = node_map[child]
            child_map[child] = True

        for root, _, _ in descriptions:
            if not child_map[root]:
                return node_map[root]

        return None
