class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mp = defaultdict(int)
        
        def solve(i, j):
            if j <= 0 or j >= i:
                return 1
            if (i, j) in mp:
                return mp[(i, j)]
            mp[(i, j)] = solve(i - 1, j - 1) + solve(i - 1, j)
            return mp[(i, j)]
        
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = solve(i, j)
            res.append(row)
        
        return res
