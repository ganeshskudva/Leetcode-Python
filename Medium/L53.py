class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val, dp = [float('-inf')], defaultdict(int)

        def solve(idx):
            if idx == len(nums) - 1:
                max_so_far = nums[idx]
            elif idx in dp:
                max_so_far = dp[idx]
            else:
                max_so_far = max(nums[idx], nums[idx] + solve(idx + 1))
            max_val[0] = max(max_val[0], max_so_far)
            return max_so_far

        solve(0)
        return 0 if max_val[0] == float('-inf') else max_val[0]
        
