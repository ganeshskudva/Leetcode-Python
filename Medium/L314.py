class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        mp, q = defaultdict(list), deque()
        q.append((root, 0))

        while q:
            node, col = q.popleft()
            mp[col].append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        return [mp[k] for k in sorted(mp)]
