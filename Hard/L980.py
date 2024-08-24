class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        x, y, empty = 0, 0, 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(grid), len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    empty += 1
                elif grid[i][j] == 1:
                    x, y = i, j

        def isValid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] != -1

        def solve(i, j, cnt):
            if not isValid(i, j):
                return 0
            if grid[i][j] == 2:
                if cnt == empty:
                    return 1
                else:
                    return 0
            grid[i][j] = -1
            tot = 0
            for d in dirs:
                tot += solve(i + d[0], j + d[1], cnt + 1)
            grid[i][j] = 0

            return tot

        return solve(x, y, -1)
