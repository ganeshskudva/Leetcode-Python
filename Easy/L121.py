class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)
        
        def solve(i, k, buy=True):
            if i >= len(prices) or k <= 0:
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            if buy:
                dp[(i, buy)] = max(-prices[i] + solve(i + 1, k, not buy), solve(i + 1, k, buy))
            else:
                dp[(i, buy)] = max(prices[i] + solve(i + 1, k - 1, not buy), solve(i + 1, k, buy))
            
            return dp[(i, buy)]
        
        return solve(0, 1)
        
