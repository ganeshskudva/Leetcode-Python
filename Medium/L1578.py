class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        dp = defaultdict(int)

        def solve(idx):
            if idx == len(colors) - 1:
                dp[idx] = 0
                return 0

            if idx in dp:
                return dp[idx]

            if colors[idx] == colors[idx + 1]:
                if neededTime[idx + 1] < neededTime[idx]:
                    neededTime[idx + 1], neededTime[idx] = neededTime[idx], neededTime[idx + 1]
                dp[idx] = min(neededTime[idx], neededTime[idx + 1]) + solve(idx + 1)
            else:
                dp[idx] = solve(idx + 1)

            return dp[idx]

        return solve(0)
