from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()  # Set to track elements we have seen so far

        # Iterate through each element in the array
        for v in arr:
            # Check if `2 * v` (double of current) or `v // 2` (half of current, if even) exists in `seen`
            if 2 * v in seen or (v % 2 == 0 and v // 2 in seen):
                return True  # If found, return True immediately
            # Add the current value to the set for future checks
            seen.add(v)

        return False  # If no such pair is found, return False

# Time Complexity (TC):
# 1. Iterating through the array: O(n), where n is the length of the array.
#    - Each element is processed once in the loop.
# 2. Set operations (add and check membership): O(1) on average for each element.
# Overall TC: O(n).

# Space Complexity (SC):
# 1. Set (`seen`): O(n), where n is the length of the array, as at most all elements can be added to the set.
# 2. Other variables (`v` and loop counters): O(1).
# Overall SC: O(n).
