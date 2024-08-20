class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = defaultdict(int)
        
        def solve(idx, mx):
            if idx >= len(piles):
                return 0
            key = (idx, mx)
            if key in dp:
                return dp[key]
            
            if idx + (2*mx) >= len(piles):
                dp[key] = sum([piles[x] for x in range(idx, len(piles))])
                return dp[key]
            
            tot, val = 0, float('-inf')
            for i in range(1, (mx * 2) + 1):
                tot += piles[idx + i - 1]
                val = max(val, tot - solve(idx + i, max(mx, i)))
            dp[key] = val
            return dp[key]
        
        value = solve(0, 1)
        return (sum(piles) + value) // 2
