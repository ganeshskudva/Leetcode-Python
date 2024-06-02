class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n, vis, cnt = len(grid), len(grid[0]), set(), 0

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == '1'

        def solve(x, y):
            if not is_valid(x, y):
                return
            if (x, y) in vis:
                return
            vis.add((x, y))

            for d in dirs:
                solve(x + d[0], y + d[1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in vis:
                    solve(i, j)
                    cnt += 1

        return cnt
