class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def on_boundary(x, y):
            return x == 0 or x == m - 1 or y == 0 or y == n - 1

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

        def solve(x, y):
            grid[x][y] = 0
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y):
                    solve(new_x, new_y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and on_boundary(i, j):
                    solve(i, j)

        return sum(sum(row) for row in grid)
