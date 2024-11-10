from collections import defaultdict
from typing import Optional

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge case: if the tree is empty, return None
        if not root:
            return None

        # Dictionary to store the depth of each node
        mp = defaultdict(int)

        # Recursive helper function to calculate the depth of each node
        def solve(node):
            if not node:
                return 0
            # If the depth of the node is not calculated yet, compute it
            if node not in mp:
                mp[node] = 1 + max(solve(node.left), solve(node.right))
            return mp[node]

        # Calculate the depth of the left and right subtrees
        left, right = solve(root.left), solve(root.right)

        # If depths of left and right subtrees are equal, current node is the LCA of deepest leaves
        if left == right:
            return root

        # Recur on the subtree with greater depth
        return self.lcaDeepestLeaves(root.right) if left < right else self.lcaDeepestLeaves(root.left)

# Time Complexity (TC): O(n)
# - The solve function is called once per node, calculating and storing the depth in O(n) time.
# - The recursive calls to find the LCA process each node, also in O(n) time.
# - Therefore, the overall time complexity is O(n).

# Space Complexity (SC): O(n)
# - The mp dictionary stores depth values for each node, taking up O(n) space.
# - The recursion stack depth can go up to O(h) where h is the height of the tree.
# - In the worst case, h = n (for a skewed tree), leading to O(n) space.
# - Overall, the space complexity is O(n).
