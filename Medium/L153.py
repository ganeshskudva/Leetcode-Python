class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi, mid, n = 0, len(nums) - 1, 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = (mid + 1) % n

        return nums[lo]
