class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n, lo, hi = len(nums), min(nums), max(nums)

        def calc(midd, kth):
            i = 0
            while i < n:
                if nums[i] <= midd:
                    kth -= 1
                    i += 2
                else:
                    i += 1
                if kth == 0:
                    return True
            return kth == 0

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if calc(mid, k):
                hi = mid
            else:
                lo = mid + 1
        return lo
