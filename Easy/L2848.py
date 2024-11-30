from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # Array to keep track of increments and decrements for ranges
        v = [0] * 102  # 102 to handle ranges up to 100 + 1 safely
        ans = 0  # Variable to store the total number of unique points
        sum_ = 0  # Variable to keep track of the current count at each point

        # Update the array `v` to mark increments at start and decrements at end+1
        for n in nums:
            v[n[0]] += 1       # Increment at the start of the range
            v[n[1] + 1] -= 1   # Decrement after the end of the range

        # Iterate over the valid range (1 to 100) to count unique points
        for i in range(1, 101):
            sum_ += v[i]  # Update the running sum
            if sum_ != 0: # If sum_ > 0, it means the point is covered by at least one range
                ans += 1

        return ans

# Time Complexity (TC):
# 1. Iterating over the `nums` list to update the `v` array: O(n), where n is the number of ranges.
# 2. Iterating over the range 1 to 100 to calculate the unique points: O(100) ≈ O(1) (constant).
# Overall TC: O(n).

# Space Complexity (SC):
# 1. The `v` array requires O(102) ≈ O(1) (constant) space.
# Overall SC: O(1).

