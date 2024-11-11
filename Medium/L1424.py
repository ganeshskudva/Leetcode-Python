from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Initialize the result list and a dictionary to store elements by diagonals
        res = []
        mp = defaultdict(list)
        max_key = 0  # Tracks the maximum diagonal key encountered
        
        # Traverse each element in `nums` to populate the dictionary with diagonals
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # Each element belongs to the diagonal `i + j`
                mp[i + j].append(nums[i][j])
                # Update max_key to know the range of diagonals we need to process later
                max_key = max(max_key, i + j)
        
        # For each diagonal from 0 to max_key, add elements in reverse order
        for i in range(max_key + 1):
            # Extend `res` with the current diagonal's elements in reverse
            res.extend(mp[i][::-1])
        
        # Return the result list containing the diagonal order traversal
        return res

# Time Complexity (TC): O(N), where N is the total number of elements in `nums`.
# - We iterate over each element in `nums` to populate the dictionary, which takes O(N).
# - Extending the `res` list with each diagonal (in reverse) also takes O(N) in total.

# Space Complexity (SC): O(N), where N is the total number of elements in `nums`.
# - The dictionary `mp` stores each element by diagonal, requiring O(N) space.
# - The result list `res` stores all elements in the required order, also requiring O(N) space.
