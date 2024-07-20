class Solution:
    def restoreMatrix(self, row, col):
        m, n = len(row), len(col)
        A = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                A[i][j] = min(row[i], col[j])
                row[i] -= A[i][j]
                col[j] -= A[i][j]
        return A
