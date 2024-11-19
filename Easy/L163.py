from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []  # List to store the missing ranges
        nums.append(upper + 1)  # Append an extra boundary to handle the upper limit
        pre = lower - 1  # Initialize the previous number as one less than the lower bound

        # Iterate through the numbers, including the extra boundary
        for n in nums:
            if n == pre + 2:  # Case: Single missing number
                result.append([n - 1, n - 1])
            elif n > pre + 2:  # Case: Multiple missing numbers in a range
                result.append([pre + 1, n - 1])
            pre = n  # Update the previous number

        return result

# Time Complexity (TC):
# O(n): We iterate through the `nums` array once, where `n` is the size of the input array. 
#       Appending `upper + 1` and checking the conditions involve constant time operations.

# Space Complexity (SC):
# O(m): The `result` list may contain up to `m` ranges, where `m` is the number of missing ranges.
#       Apart from that, we use a constant amount of space for variables like `pre`.

