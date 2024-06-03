class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0

        def solve(node):
            if not node:
                return 0

            left, right = solve(node.left), solve(node.right)
            self.max_d = max(self.max_d, left + right)

            return max(left, right) + 1

        solve(root)
        return self.max_d
