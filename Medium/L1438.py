from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()  # Deques to track minimum and maximum indices
        left = 0  # Left pointer for the sliding window
        max_length = 0  # Variable to store the maximum subarray length

        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            # Maintain min_deque for the smallest element in the window
            while min_deque and nums[right] <= nums[min_deque[-1]]:
                min_deque.pop()
            # Maintain max_deque for the largest element in the window
            while max_deque and nums[right] >= nums[max_deque[-1]]:
                max_deque.pop()

            # Add the current index to both deques
            min_deque.append(right)
            max_deque.append(right)

            # Shrink the window if the difference between max and min exceeds the limit
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if min_deque[0] == left:  # Remove outdated indices from min_deque
                    min_deque.popleft()
                if max_deque[0] == left:  # Remove outdated indices from max_deque
                    max_deque.popleft()
                left += 1  # Shrink the window

            # Update the maximum subarray length
            max_length = max(max_length, right - left + 1)

        return max_length  # Return the maximum subarray length

# Time Complexity (TC):
# 1. The `right` pointer iterates over the array once: O(n), where n is the length of the array.
# 2. Each index is added and removed from the deques at most once:
#    - Adding to or removing from a deque takes O(1).
#    - This results in O(n) operations for both deques combined.
# 3. Shrinking the window by incrementing `left` also contributes O(n), as each element is processed at most once.
# Overall TC: O(n).

# Space Complexity (SC):
# 1. The two deques (`min_deque` and `max_deque`) store indices:
#    - In the worst case, each deque can store up to n indices, where n is the size of the array.
# 2. Other variables like `left`, `right`, and `max_length` use O(1) space.
# Overall SC: O(n), dominated by the space used by the deques.
