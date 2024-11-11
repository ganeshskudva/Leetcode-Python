from typing import List
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Dictionary to group strings by their "shift pattern"
        mp = defaultdict(list)

        # Iterate through each string to determine its shift pattern
        for s in strings:
            # Initialize an empty tuple to represent the shift pattern for the string
            key = ()
            
            # Calculate the shift pattern by finding the differences between adjacent characters
            for i in range(len(s) - 1):
                # Calculate the circular difference between consecutive characters
                diff = 26 + ord(s[i + 1]) - ord(s[i])
                
                # Append the difference modulo 26 to ensure it falls within [0, 25]
                key += (diff % 26,)
            
            # Append the string to the list in `mp` associated with its calculated shift pattern
            mp[key].append(s)
        
        # Return all the grouped lists of strings
        return list(mp.values())

# Time Complexity (TC):
# - For each string of length L, calculating the shift pattern takes O(L) time.
# - If there are N strings in total, the time complexity is O(N * L) to process all strings.
# - Therefore, the overall time complexity is O(N * L), where N is the number of strings and L is the average string length.

# Space Complexity (SC):
# - We use a dictionary `mp` to store groups of strings, where each group represents a unique shift pattern.
# - In the worst case, if each string has a unique shift pattern, `mp` will store N entries, each containing one string, resulting in O(N) space.
# - Each string and its calculated shift pattern (tuple) occupy O(L) space, so the overall space complexity is O(N * L).
