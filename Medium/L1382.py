class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_lst = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_lst.append(node)
            inorder(node.right)

        def create_tree(start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            new_root = sorted_lst[mid]
            new_root.left = create_tree(start, mid - 1)
            new_root.right = create_tree(mid + 1, end)
            return new_root

        inorder(root)
        return create_tree(0, len(sorted_lst) - 1)
