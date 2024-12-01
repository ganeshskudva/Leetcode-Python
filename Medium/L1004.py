class Solution:
    def longestOnes(self, nums, k):
        left, tot = 0, 0  # Initialize the left pointer for the window and 'tot' for the max length

        for right in range(len(nums)):  # Iterate through the array with the right pointer
            if nums[right] == 0:  # If the current element is 0, decrement k (using one flip)
                k -= 1
            if k < 0:  # If k goes negative, it means we've exceeded the allowed number of flips
                if nums[left] == 0:  # If the left element is 0, increment k back (reclaim the flip as we move left)
                    k += 1
                left += 1  # Move the left pointer to shrink the window

            tot = max(tot, right - left + 1)  # Update the maximum window size

        return tot  # Return the maximum size of the window that can have at most k 0s

# Time Complexity (TC):
# 1. The outer loop iterates through the array with the right pointer: O(n), where n is the length of the array.
# 2. The inner adjustment of the left pointer moves incrementally, and each element is processed at most once by the left pointer.
# 3. Each element is processed at most twice (once by the right pointer and once by the left pointer).
# Overall TC: O(n).

# Space Complexity (SC):
# 1. The algorithm uses a constant amount of extra space:
#    - Two integer variables `left` and `tot` for the sliding window management and result tracking.
#    - The variable `k` is also constant space.
# 2. No additional data structures are required.
# Overall SC: O(1).
