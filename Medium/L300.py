class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mp, ans = defaultdict(int), 0
        
        @cache
        def solve(idx):
            if idx >= len(nums):
                return 0
            
            if idx in mp:
                return mp[idx]
            
            res = 0
            for i in range(idx + 1, len(nums)):
                if nums[i] > nums[idx]:
                    res = max(res, 1 + solve(i))
            
            mp[idx] = res
            return mp[idx]
        
        for index in range(len(nums)):
            ans = max(ans, 1 + solve(index))
        return ans
