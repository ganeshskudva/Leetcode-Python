from collections import defaultdict
from typing import List

class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        # Step 1: Initialize a defaultdict to track brightness changes at specific positions.
        brightness_changes = defaultdict(int)

        # Step 2: For each light at position 'idx' with range 'dis', mark the start and end of its effect.
        for idx, dis in lights:
            # Mark where the light starts affecting brightness and where it stops.
            brightness_changes[max(0, idx - dis)] += 1
            brightness_changes[min(n, idx + dis + 1)] -= 1

        # Step 3: Traverse the positions and calculate brightness with a single pass.
        current_brightness, count = 0, 0

        # Step 4: Accumulate brightness values and check if the requirement is met.
        for i in range(n):
            current_brightness += brightness_changes[i]  # Apply brightness changes
            if current_brightness >= requirement[i]:     # Check if brightness meets the requirement
                count += 1                               # Increment count if the requirement is met

        # Step 5: Return the total count of positions that meet the brightness requirement.
        return count

# Time Complexity (TC):
# 1. Looping through the 'lights' list takes O(m), where 'm' is the number of lights.
# 2. Looping through the positions (0 to n-1) takes O(n).
# 
# Overall, the time complexity is O(m + n), where:
# - 'm' is the number of lights,
# - 'n' is the total number of positions.

# Space Complexity (SC):
# 1. The dictionary 'brightness_changes' stores brightness adjustments for up to O(n) positions.
# 2. Additional variables 'current_brightness' and 'count' take constant space.
# 
# Therefore, the space complexity is O(n).
