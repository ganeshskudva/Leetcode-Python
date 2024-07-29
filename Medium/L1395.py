class Solution:
    def numTeams(self, rating):
        n = len(rating)
        dp = [[[-1 for _ in range(3)] for _ in range(4)] for _ in range(n)]

        def solve(idx, taken, state):
            if taken == 3:
                return 1
            if dp[idx][taken][state] != -1:
                return dp[idx][taken][state]

            ans = 0
            ele = rating[idx]
            for i in range(idx + 1, n):
                if state == 0:
                    if ele < rating[i]:
                        ans += solve(i, taken + 1, 1)
                    elif ele > rating[i]:
                        ans += solve(i, taken + 1, 2)
                elif state == 1:
                    if ele < rating[i]:
                        ans += solve(i, taken + 1, 1)
                elif state == 2:
                    if ele > rating[i]:
                        ans += solve(i, taken + 1, 2)

            dp[idx][taken][state] = ans
            return ans

        ans = 0
        for i in range(n - 2):
            ans += solve(i, 1, 0)

        return ans
