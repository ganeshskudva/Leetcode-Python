class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        
        if tot % 2 != 0:
            return False
        tot, dp = tot // 2, defaultdict(int)
        
        def solve(idx, total_sum):
            if not total_sum:
                return True
            
            if idx >= len(nums) or total_sum < 0:
                return False
            key = (idx, total_sum)
            if key in dp:
                return dp[key]
            
            dp[key] = solve(idx + 1, total_sum - nums[idx]) or solve(idx + 1, total_sum)
            return dp[key]
        
        return solve(0, tot)
