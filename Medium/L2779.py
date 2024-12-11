from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array to enable the sliding window approach
        nums.sort()
        
        # Initialize the starting pointer of the sliding window and the answer
        start = 0
        ans = 0
        
        # Step 2: Iterate through the array with the sliding window
        for i in range(len(nums)):
            # nums[i] represents the current maximum in the window
            # nums[start] represents the current minimum in the window

            # If the current window is invalid, shrink it by moving the `start` pointer
            while nums[i] - nums[start] > 2 * k:
                start += 1  # Move the `start` pointer forward

            # The current window [start ... i] is valid; calculate its size
            # Update `ans` with the maximum size of the valid window
            ans = max(ans, i - start + 1)
        
        # Return the maximum size of the valid window as the result
        return ans

# Time Complexity (TC):
# 1. Sorting the array: O(n log n), where n is the length of the input array `nums`.
# 2. Sliding window iteration: O(n), as each element is processed at most twice
#    (once when expanding the window and once when shrinking it with `start`).
# Overall TC: O(n log n) due to the sorting step.

# Space Complexity (SC):
# - Sorting is done in-place, so no additional storage is required for sorting: O(1).
# - Only a few variables (`start`, `ans`, and the loop variables) are used.
# Overall SC: O(1) extra space.
