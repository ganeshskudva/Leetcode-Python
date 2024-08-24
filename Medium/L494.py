class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def solve(idx, curr_sum=0):
            if idx < 0:
                if curr_sum == target:
                    return 1
                return 0
            key = (idx, curr_sum)
            if key in dp:
                return dp[key]
            
            dp[key] = solve(idx - 1, curr_sum + nums[idx]) + solve(idx - 1, curr_sum - nums[idx])
            return dp[key]
        
        return solve(len(nums) - 1)
