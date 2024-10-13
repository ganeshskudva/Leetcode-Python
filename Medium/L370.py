from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Step 1: Initialize the result array `res` with zeroes, having the same length as the target array.
        # This array will hold the difference values and later be transformed into the final result.
        res = [0] * length

        # Step 2: Process each update in the updates list.
        # Each update contains `start`, `end`, and `diff` which means:
        # We need to add `diff` to the range [start, end].
        for start, end, diff in updates:
            # Increment the `start` index by `diff` because the range starts at this index.
            res[start] += diff
            
            # If `end + 1` is within the bounds of the array, decrement the value at index `end + 1` by `diff`.
            # This marks the end of the range because the effect of `diff` should stop after the `end` index.
            if end + 1 < length:
                res[end + 1] -= diff

        # Step 3: Manually accumulate the values by converting the difference array into the final result.
        # This step essentially computes the cumulative sum across the `res` array.
        for i in range(1, length):
            res[i] += res[i - 1]

        # Return the final modified array.
        return res

# Time Complexity (TC):
# 1. Initializing the result array `res` with zeroes takes O(n), where n is the length of the array.
# 2. Processing each update takes O(1) per update. Since there are `u` updates, this step takes O(u).
# 3. Manually accumulating the values (computing the cumulative sum) takes O(n), as we traverse the entire array once.
# Therefore, the overall time complexity is O(n + u), where `n` is the length of the array and `u` is the number of updates.

# Space Complexity (SC):
# 1. The `res` array takes O(n) space, where `n` is the length of the array.
# 2. No additional data structures are used, so the space complexity is dominated by the size of the result array.
# Therefore, the overall space complexity is O(n).
