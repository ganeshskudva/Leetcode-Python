class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] != 0

        def solve(x, y):
            if not is_valid(x, y):
                return 0

            curr, max_gold = grid[x][y], 0
            grid[x][y] = 0
            for d in dirs:
                max_gold = max(max_gold, solve(x + d[0], y + d[1]))

            grid[x][y] = curr
            return grid[x][y] + max_gold
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, solve(i, j))
        
        return res
        
