class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = {}

        def solve(idx, buy):
            if idx >= len(prices):
                return 0

            key = (idx, buy)
            if key in mp:
                return mp[key]

            if buy:
                mp[key] = max(-prices[idx] + solve(idx + 1, False), solve(idx + 1, True))
            else:
                mp[key] = max(prices[idx] + solve(idx + 1, True), solve(idx + 1, False))

            return mp[key]

        return solve(0, True)
