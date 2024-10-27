from functools import cache
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeQueries(self, root, queries) -> List[int]:
        # Function to calculate the height of each subtree
        @cache
        def height(r):
            return 1 + max(height(r.left), height(r.right)) if r else 0

        # Depth-first search to calculate the answer for each node
        ans = {}  # Local variable instead of parameter

        def dfs(r, depth=0, mx=0):
            if not r:
                return
            ans[r.val] = mx  # Store the maximum path length seen so far for node r
            # Traverse left and right children, updating the max depth without each child
            dfs(r.left, depth + 1, max(mx, depth + height(r.right)))
            dfs(r.right, depth + 1, max(mx, depth + height(r.left)))

        dfs(root)  # Start DFS traversal from the root
        # For each query node, return the precomputed answer from `ans`
        return [ans[v] for v in queries]

# Time Complexity (TC): O(n), as explained in the original solution.
# Space Complexity (SC): O(n), with slight reduction in parameter overhead.
