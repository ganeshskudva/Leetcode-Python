class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, ans, mp = len(bombs), 0, defaultdict(list)

        def is_within_range(x1, y1, x2, y2, r):
            return r ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if is_within_range(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1], bombs[i][2]):
                    mp[i].append(j)

        def dfs(node, visited):
            for child in mp[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(n):
            vis = set([i])
            dfs(i, vis)
            ans = max(ans, len(vis))

        return ans
