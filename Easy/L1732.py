from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Step 1: Initialize variables
        # 'mx' will store the maximum altitude reached.
        # 'val' is the current altitude, starting from 0.
        mx, val = 0, 0
        
        # Step 2: Traverse the 'gain' list to calculate altitudes.
        # For each 'g' in the gain list, add it to 'val' (current altitude)
        # and update 'mx' if the current altitude exceeds the maximum altitude seen so far.
        for g in gain:
            val += g  # Update current altitude
            mx = max(mx, val)  # Update the maximum altitude
        
        # Step 3: Return the maximum altitude reached during the hike.
        return mx

# Time Complexity (TC):
# 1. The for loop iterates over the entire 'gain' list, which takes O(n) time, where 'n' is the length of the 'gain' list.
# 2. Each operation inside the loop (addition and max check) takes constant time O(1).
# Therefore, the overall time complexity is O(n), where 'n' is the length of the 'gain' list.

# Space Complexity (SC):
# 1. The space complexity is O(1), as we are using only a few variables ('mx', 'val') regardless of the size of the input list.
# 2. The input list 'gain' is not modified, and no additional data structures are used.
# Therefore, the overall space complexity is O(1).
