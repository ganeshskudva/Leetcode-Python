class Solution:
    def numDecodings(self, s: str) -> int:
        mp = {}

        def valid(idx):
            if s[idx] == "1" or s[idx] == "2" and int(s[idx + 1]) < 7:
                return True

            return False

        def solve(idx):
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0
            if idx in mp:
                return mp[idx]

            way = solve(idx + 1)
            if idx < len(s) - 1:
                if valid(idx):
                    way += solve(idx + 2)

            mp[idx] = way
            return way

        return solve(0)
