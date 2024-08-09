class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        mp = {}

        def solve(idx, k, buy=True):
            if idx >= len(prices) or k <= 0:
                return 0

            key = (idx, buy, k)
            if key in mp:
                return mp[key]

            if buy:
                mp[key] = max(-prices[idx] + solve(idx + 1, k, not buy), solve(idx + 1, k, buy))
            else:
                mp[key] = max(prices[idx] + solve(idx + 1, k - 1, not buy), solve(idx + 1, k, buy))

            return mp[key]

        return solve(0, k)
