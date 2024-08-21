class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
        mp = defaultdict(float)
        
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n

        def solve(kth, r, c):
            if not is_valid(r, c):
                return 0
            if kth == 0:
                return 1
            key = (r, c, kth)
            if key in mp:
                return mp[key]

            rate = float(0)
            for d in dirs:
                rate += 0.125 * solve(kth - 1, r + d[0], c + d[1])

            mp[key] = rate
            return mp[key]

        return solve(k, row, column)
