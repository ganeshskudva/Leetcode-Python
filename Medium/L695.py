class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis, tot = set(), 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

        def solve(x, y):
            if not is_valid(x, y):
                return 0
            if (x, y) in vis:
                return 0

            vis.add((x, y))
            cnt = 0
            for d in dirs:
                cnt += solve(x + d[0], y + d[1])

            return cnt + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in vis:
                    tot = max(tot, solve(i, j))

        return tot
