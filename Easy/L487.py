class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, k, mx = 0, 1, float('-inf')  # Initialize left pointer for the window, k for allowed flips, and mx for max length

        for right in range(len(nums)):  # Iterate over nums with the right pointer
            if nums[right] == 0:  # If the current element is 0, decrement k (using one flip)
                k -= 1
            if k < 0:  # If k goes negative, it means we've exceeded the allowed number of flips
                if nums[left] == 0:  # If the left element is 0, increment k back (reclaim the flip as we move left)
                    k += 1
                left += 1  # Move the left pointer to shrink the window

            mx = max(mx, right - left + 1)  # Update the maximum window size that can have at most one 0

        return 0 if mx == float('-inf') else mx  # If no valid window was found, return 0, otherwise return the maximum length

# Time Complexity (TC):
# 1. The outer loop iterates through the array with the right pointer: O(n), where n is the length of the array.
# 2. The inner adjustments for the left pointer move incrementally, and each element is processed at most once by the left pointer.
# 3. As each element is processed at most twice (once by the right pointer and once by the left pointer), the total time complexity is O(n).
# Overall TC: O(n).

# Space Complexity (SC):
# 1. The algorithm uses a constant amount of extra space:
#    - Three variables `left`, `k`, and `mx` are used to manage the sliding window and track results.
# 2. No additional data structures are required.
# Overall SC: O(1).

