from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, tot, k = len(nums), 0, 0  # Initialize length of nums, running total, and query counter
        freq = [0] * (n + 1)  # Difference array for efficient range updates

        for i in range(n):  # Iterate through nums
            # Ensure enough cumulative value to zero out nums[i]
            while tot + freq[i] < nums[i]:  # If current total is insufficient
                if k == len(queries):  # No more queries to process
                    return -1  # Impossible to zero out the array
                
                l, r, v = queries[k][0], queries[k][1], queries[k][2]  # Get the next query
                k += 1  # Increment query counter

                if r < i:  # If the query range is entirely before index i
                    continue  # Skip this query
                
                # Apply the query effect using the difference array
                if l >= i:  # Only apply if the query starts at or after i
                    freq[l] += v
                freq[r + 1] -= v  # Mark the end of the query range

            tot += freq[i]  # Update the cumulative total

        return k  # Return the number of queries used

# Time Complexity (TC):
# 1. Processing `nums` array:
#    - The outer loop runs for O(n), where n is the size of `nums`.
# 2. Processing queries:
#    - Each query is processed at most once, so this step takes O(m), where m is the number of queries.
# 3. Updates to `freq`:
#    - Updates to the `freq` array for each query are constant time, O(1).
# Overall TC: O(n + m), as both arrays are iterated through at most once.

# Space Complexity (SC):
# 1. Difference array (`freq`):
#    - The `freq` array has size O(n + 1), used for efficient range updates.
# 2. Other variables:
#    - Variables like `tot`, `k`, and loop counters use O(1) space.
# Overall SC: O(n), dominated by the `freq` array.
