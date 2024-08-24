class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mp = {}

        def solve(idx, currProduct):
            if idx >= len(nums):
                return currProduct

            key = (idx, currProduct)
            if key in mp:
                return mp[key]

            mp[key] = max(currProduct, solve(idx + 1, nums[idx] * currProduct), solve(idx + 1, nums[idx]))
            return mp[key]

        return solve(1, nums[0])
