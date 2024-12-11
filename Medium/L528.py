import random
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        # Compute prefix sums for the weights
        # self.prefix_sums[i] represents the cumulative sum of weights from index 0 to i
        self.prefix_sums = list(w)
        for i in range(1, len(w)):
            self.prefix_sums[i] += self.prefix_sums[i - 1]

    def pickIndex(self) -> int:
        # Generate a random integer between 1 and the total weight (inclusive)
        target = random.randint(1, self.prefix_sums[-1])

        # Perform binary search to find the smallest index such that prefix_sums[index] >= target
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2  # Calculate the middle index
            if self.prefix_sums[mid] < target:
                left = mid + 1  # Narrow the search to the right half
            else:
                right = mid  # Narrow the search to the left half
        return left  # The index where the target falls in the prefix sums

# Time Complexity (TC):
# 1. `__init__`:
#    - Computing prefix sums requires O(n), where n is the length of the input array `w`.
# 2. `pickIndex`:
#    - The binary search runs in O(log(n)), where n is the number of weights.
# Overall:
#    - Initialization: O(n)
#    - Each call to `pickIndex`: O(log(n))

# Space Complexity (SC):
# 1. The `prefix_sums` list requires O(n) space to store the cumulative weights.
# 2. No additional data structures are used in the `pickIndex` method.
# Overall: O(n)
