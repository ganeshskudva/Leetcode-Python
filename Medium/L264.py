class Solution:
    def nthUglyNumber(self, n: int) -> int:
        mp = {}
        mp[0] = 1
        self.index2, self.index3, self.index5 = 0, 0, 0

        def solve(idx, f2, f3, f5):
            if idx >= n:
                return
            if idx in mp:
                return mp[idx]
            mini = min(min(f2, f3), f5)
            mp[idx] = mini
            if f2 == mini:
                self.index2 += 1
                f2 = 2 * mp[self.index2]

            if f3 == mini:
                self.index3 += 1
                f3 = 3 * mp[self.index3]

            if f5 == mini:
                self.index5 += 1
                f5 = 5 * mp[self.index5]

            solve(idx + 1, f2, f3, f5)

        solve(1, 2, 3, 5)
        return mp[n - 1]
