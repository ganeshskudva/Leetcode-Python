class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Finds the largest value in each row of a binary tree.
        Optimized to minimize unnecessary calculations.
        """
        if not root:
            return []
        
        res = []
        q = deque([root])
        while q:
            max_ = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                max_ = max(node.val, max_)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(max_)
        
        return res

"""
Time Complexity (TC):
- O(N), where N is the number of nodes in the tree. Each node is visited once.

Space Complexity (SC):
- O(W), where W is the maximum width of the tree. This is the maximum number of nodes at any level of the tree, which corresponds to the size of the queue.
"""