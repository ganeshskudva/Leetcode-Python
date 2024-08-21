class Solution:
    def strangePrinter(self, s: str) -> int:
        dp = {}
        
        def solve(left, right):
            if left == right:
                return 1
            key = (left, right)
            if key in dp:
                return dp[key]
            
            res = float('inf')
            for i in range(left, right):
                res = min(res, solve(left, i) + solve(i + 1, right))
            if s[left] == s[right]:
                res -= 1
            
            dp[key] = res
            return res
        
        return solve(0, len(s) - 1)
