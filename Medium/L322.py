class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp, n = defaultdict(int), len(coins)
        
        def solve(idx, amt):
            if idx >= n or amt <= 0:
                return 0 if not amt else float('inf')
            
            key = (idx, amt)
            if key in dp:
                return dp[key]
            
            res = -1
            if coins[idx] > amt:
                dp[key] = solve(idx + 1, amt)
            else:
                dp[key] = min(solve(idx + 1, amt), 1 + solve(idx, amt - coins[idx]))
            
            return dp[key]
        
        res = solve(0, amount)
        return -1 if res == float('inf') else res
