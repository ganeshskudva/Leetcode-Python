from functools import lru_cache
from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Cache for storing the length of longest increasing/decreasing subsequence
        # from each element towards the left or right
        
        # Left-to-right increasing sequence ending at index i
        @lru_cache(None)
        def left_increasing(i: int) -> int:
            max_len = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, left_increasing(j) + 1)
            return max_len

        # Right-to-left decreasing sequence starting at index i
        @lru_cache(None)
        def right_decreasing(i: int) -> int:
            max_len = 1
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    max_len = max(max_len, right_decreasing(j) + 1)
            return max_len

        # Calculate the maximum length of a valid mountain sequence
        max_mountain = 0
        for i in range(1, len(nums) - 1):
            left = left_increasing(i)
            right = right_decreasing(i)
            if left > 1 and right > 1:
                max_mountain = max(max_mountain, left + right - 1)

        # Result is the total number of elements minus the maximum mountain sequence length
        return len(nums) - max_mountain

# Time Complexity (TC):
# - Calculating `left_increasing` and `right_decreasing` for each element has a worst-case complexity of O(N^2),
#   where N is the length of `nums`. This is because each function computes the LIS or LDS with memoization.

# Space Complexity (SC):
# - Space complexity is O(N) for the cache (memoization) and O(N) for the recursive stack in the worst case.
# - Thus, the overall space complexity is O(N).
