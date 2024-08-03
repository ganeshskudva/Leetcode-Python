class Solution:
    def numTrees(self, n: int) -> int:
        mp = defaultdict(int)

        def solve(n):
            if n <= 1:
                return 1
            if n in mp:
                return mp[n]
            for i in range(1, n + 1):
                mp[n] += solve(i - 1) * solve(n - i)
            return mp[n]

        return solve(n)
