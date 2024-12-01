class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0  # Left pointer for the sliding window
        max_length = 0  # Maximum subarray length
        flips_remaining = 1  # Number of 0s that can be flipped

        for right in range(len(nums)):  # Iterate with the right pointer
            if nums[right] == 0:  # Use a flip for a 0
                flips_remaining -= 1

            # If flips are exhausted, shrink the window from the left
            while flips_remaining < 0:
                if nums[left] == 0:  # Reclaim the flip
                    flips_remaining += 1
                left += 1  # Move the left pointer to shrink the window

            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)

        return max_length - 1  # Subtract 1 as we need to delete one element

# Time Complexity (TC):
# 1. The outer loop (right pointer) iterates over the array once: O(n), where n is the length of the array.
# 2. The inner loop (left pointer) adjusts only when the number of flips becomes invalid:
#    - Each element is processed at most once by the left pointer.
#    - Combined, the left and right pointers process each element at most twice.
# Overall TC: O(n).

# Space Complexity (SC):
# 1. The algorithm uses a constant number of variables:
#    - `left`, `max_length`, and `flips_remaining` for managing the sliding window and tracking results.
# 2. No additional data structures are used, and the operations are performed in place.
# Overall SC: O(1).
