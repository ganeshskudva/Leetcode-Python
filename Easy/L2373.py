class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0 for j in range(n - 2)] for i in range(n - 2)]

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                tmp = 0

                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        tmp = max(tmp, grid[k][l])
                
                res[i - 1][j - 1] = tmp
        
        return res
        
