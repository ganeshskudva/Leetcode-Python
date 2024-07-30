class Solution:
    def climbStairs(self, n: int) -> int:
        mp = {0: 0, 1: 1, 2: 2}

        def solve(n):
            if n in mp:
                return mp[n]

            mp[n] = solve(n - 1) + solve(n - 2)
            return mp[n]

        return solve(n)
