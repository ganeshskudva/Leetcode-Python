class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connected = [[False] * n for _ in range(n)]
        cnts = [0] * n
        for r in roads:
            cnts[r[0]] += 1
            cnts[r[1]] += 1
            connected[r[0]][r[1]] = True
            connected[r[1]][r[0]] = True  # cache if i and j are directly connected

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, cnts[i] + cnts[j] - (1 if connected[i][j] else 0))  # loop all pairs

        return res