class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = {}

        def solve(idx, buy=True):
            if idx >= len(prices):
                return 0
            key = (idx, buy)
            if key in mp:
                return mp[key]

            if buy:
                mp[key] = max(-prices[idx] + solve(idx + 1, not buy), solve(idx + 1, buy))
            else:
                mp[key] = max(prices[idx] + solve(idx + 2, not buy), solve(idx + 1, buy))
            return mp[key]

        return solve(0)
