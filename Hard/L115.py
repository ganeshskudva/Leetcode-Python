class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = {}
        
        def solve(idx_s=0, idx_t=0):
            if idx_t == m:
                return 1
            if idx_s == n:
                return 0
            key = (idx_s, idx_t)
            if key in dp:
                return dp[key]
            
            if s[idx_s] == t[idx_t]:
                dp[key] = solve(idx_s + 1, idx_t + 1) + solve(idx_s + 1, idx_t)
            else:
                dp[key] = solve(idx_s + 1, idx_t)

            return dp[key]
        
        return solve()
