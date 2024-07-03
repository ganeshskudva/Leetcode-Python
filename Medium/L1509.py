class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        i, n, lo = 0, len(nums), float('inf')
        j = n - 4
        while 0 <= j < n:
            lo = min(lo, nums[j] - nums[i])
            i, j = i + 1, j + 1
        return 0 if lo == float('inf') else lo
