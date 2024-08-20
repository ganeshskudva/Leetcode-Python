class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = defaultdict(int)

        @cache
        def solve(idx, turn=True):
            if idx >= len(stoneValue):
                return 0
            key = (idx, turn)
            if key in dp:
                return dp[key]

            tot, next_turn = 0, not turn
            if turn:
                res = float('-inf')
                for i in range(idx, min(idx + 3, len(stoneValue))):
                    tot += stoneValue[i]
                    res = max(res, tot + solve(i + 1, next_turn))
            else:
                res = float('inf')
                for i in range(idx, min(idx + 3, len(stoneValue))):
                    tot += stoneValue[i]
                    res = min(res, solve(i + 1, next_turn) - tot)

            dp[key] = res
            return dp[key]

        val = solve(0)
        return "Bob" if val < 0 else ("Alice" if val > 0 else "Tie")
