class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = defaultdict(bool)
        
        def solve(n, m):
            if n <= -1 and m <= -1:
                return True
            if n == -1 and p[m] == '*':
                return solve(n, m - 2)
            if n == -1 or m == -1:
                return False
            key = (n, m)
            if key in dp:
                return dp[key]
            
            if s[n] == p[m]:
                dp[key] = solve(n - 1, m - 1)
            else:
                if p[m] == '*':
                    if s[n] == p[m - 1] or p[m - 1] == '.':
                        dp[key] = solve(n - 1, m) or solve(n, m - 2)
                    else:
                        dp[key] = solve(n, m - 2)
                elif p[m] == '.':
                    dp[key] = solve(n - 1, m - 1)
            
            return dp[key]
        
        return solve(len(s) - 1, len(p) - 1)
