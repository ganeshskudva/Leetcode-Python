class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, left, right = nums[-1] - nums[0], nums[0] + k, nums[-1] -k
        for i in range(len(nums) - 1):
            mx, mn = max(nums[i] + k, right), min(left, nums[i + 1] - k)
            res = min(res, mx - mn)
        return res
