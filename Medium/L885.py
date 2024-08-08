class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res, length, d = [[rStart, cStart]], 0, 0

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        while len(res) < rows * cols:
            if d == 0 or d == 2:
                length += 1
            for i in range(length):
                rStart, cStart = rStart + dirs[d][0], cStart + dirs[d][1]
                if is_valid(rStart, cStart):
                    res.append([rStart, cStart])
            d = (d + 1) % 4

        return res
