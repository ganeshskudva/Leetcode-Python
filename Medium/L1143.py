class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mp = {}

        def solve(m, n):
            if m == 0 or n == 0:
                return 0

            key = (m, n)
            if key in mp:
                return mp[key]
            
            if text1[m - 1] == text2[n - 1]:
                mp[key] = 1 + solve(m - 1, n - 1)
            else:
                mp[key] = max(solve(m - 1, n), solve(m, n - 1))
            
            return mp[key]
        
        return solve(len(text1), len(text2)) 
