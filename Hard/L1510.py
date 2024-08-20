class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = defaultdict(int)

        def solve(num):
            if not num:
                return False
            if num in dp:
                return dp[num]

            res, i = False, 1
            while (i * i) <= num:
                if not solve(num - (i * i)):
                    res = True
                    break
                i += 1
            dp[num] = res
            return dp[num]

        return solve(n)
