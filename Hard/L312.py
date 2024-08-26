class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        arr = [1]
        for n in nums:
            arr.append(n)
        arr.append(1)
        n = len(nums)

        def solve(i, j):
            if i > j:
                return 0
            key = (i, j)
            if key in dp:
                return dp[key]
            res = 0
            for k in range(i, j + 1):
                cost_left = solve(i, k - 1)
                cost_last = arr[i - 1] * arr[k] * arr[j + 1]
                cost_right = solve(k + 1, j)
                res = max(res, cost_last + cost_left + cost_right)
            dp[key] = res
            return res

        return solve(1, n)
