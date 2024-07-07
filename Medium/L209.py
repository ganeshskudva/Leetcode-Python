class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        i = j = tot = 0
        minimum = float('inf')

        while j < len(nums):
            tot += nums[j]
            j += 1

            while tot >= target:
                minimum = min(minimum, j - i)
                tot -= nums[i]
                i += 1

        return 0 if minimum == float('inf') else minimum
