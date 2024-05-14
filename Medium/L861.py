class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0
        res += (1 << (n - 1)) * m

        for j in range(1, n):
            same = 0
            for i in range(m):
                if grid[i][0] == grid[i][j]:
                    same += 1
            res += (1 << (n - 1 - j)) * max(same, m - same)
        
        return res
