import collections
import sys
from typing import List

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        # Step 1: Initialize a defaultdict 'd' to track the changes in brightness at specific positions.
        # 'd' will store the brightness changes at the left and right ends of each light's range.
        d = collections.defaultdict(int)

        # Step 2: Process each light in the 'lights' list.
        # For each light with position 'i' and range 'dis':
        # - Increase brightness at position 'i - dis' (the left-end of the light's range).
        # - Decrease brightness at position 'i + dis + 1' (one position after the right-end of the range).
        for i, dis in lights:
            d[i - dis] += 1                           # The light starts increasing brightness at this position
            d[i + dis + 1] -= 1                       # The light stops affecting brightness just after this position

        # Step 3: Initialize variables to track:
        # - 'cur' for the current brightness level.
        # - 'max_idx' for the position with the maximum brightness.
        # - 'max_val' for the highest brightness value found so far.
        cur, max_idx, max_val = 0, -1, -sys.maxsize

        # Step 4: Sort the dictionary by position (key) and accumulate the brightness values.
        # As we traverse through the sorted positions, we accumulate brightness changes.
        for idx, val in sorted(d.items()):            # Sort the positions by key
            cur += val                                # Add the brightness change at the current position

            # Step 5: If the current brightness is higher than the maximum brightness recorded so far,
            # update the maximum brightness and the corresponding index (position).
            if cur > max_val:
                max_val, max_idx = cur, idx

        # Step 6: Return the position with the maximum brightness.
        return max_idx

# Time Complexity (TC):
# 1. The loop over 'lights' to update the dictionary 'd' runs in O(m), where 'm' is the number of lights.
#    For each light, we perform two updates to the dictionary.
# 2. Sorting the dictionary 'd' by keys takes O(k log k), where 'k' is the number of unique positions affected by the lights.
# 3. Iterating over the sorted dictionary to accumulate brightness takes O(k), where 'k' is the number of unique positions.

# Overall, the time complexity is O(m + k log k), where:
#   - 'm' is the number of lights,
#   - 'k' is the number of unique positions affected by the lights.

# Space Complexity (SC):
# 1. The dictionary 'd' stores O(k) unique positions, where 'k' is the number of unique positions.
# 2. We use constant space for a few additional variables ('cur', 'max_idx', 'max_val').
# 3. No other data structures are used that scale with the input size.

# Therefore, the overall space complexity is O(k), where 'k' is the number of unique positions.
