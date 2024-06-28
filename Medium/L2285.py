class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg, res = [0] * n, 0
        for start, dest in roads:
            deg[start], deg[dest] = deg[start] + 1, deg[dest] + 1

        deg.sort()
        for i in range(n):
            res += deg[i] * (i + 1)
        return res
