class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mp = {}

        def solve(m, n):
            key = (m, n)
            if m == 0:
                mp[key] = n
                return mp[key]

            if n == 0:
                mp[key] = m
                return mp[key]

            if key in mp:
                return mp[key]

            if word1[m - 1] == word2[n - 1]:
                return solve(m - 1, n - 1)

            insert, delete, replace = solve(m, n - 1), solve(m - 1, n), solve(m - 1, n - 1)

            mp[key] = 1 + min(insert, delete, replace)
            return mp[key]

        return solve(len(word1), len(word2))
