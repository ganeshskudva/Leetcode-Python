class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, mid, hi = 0, 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1
