import random
from typing import List

class Solution:
    
    def __init__(self, w: List[int]):
        # Precompute cumulative weights
        self.w_sums = [0] * len(w)  # Array to store cumulative sums of weights
        self.w_sums[0] = w[0]
        
        # Build the cumulative sum array where each index `i` in `w_sums` represents the sum of weights up to `w[i]`
        for i in range(1, len(w)):
            self.w_sums[i] = self.w_sums[i - 1] + w[i]

    def pickIndex(self) -> int:
        # Randomly select a target index in the range of the total sum of weights
        n, rand_idx = len(self.w_sums), random.randint(1, self.w_sums[-1])
        
        # Use binary search to find the index corresponding to the selected random weight
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2
            # Check if mid index matches the random target, else adjust search range
            if self.w_sums[mid] == rand_idx:
                return mid
            elif self.w_sums[mid] < rand_idx:
                left = mid + 1
            else:
                right = mid

        return left

# Time Complexity (TC):
# - __init__ (constructor): O(n), where n is the length of the weight list `w`.
#   This is due to the cumulative sum calculation, which iterates over the weights once.
# - pickIndex method: O(log n) for the binary search, as we use binary search to find the target index within `w_sums`.

# Space Complexity (SC):
# - O(n) for storing the cumulative sums array `w_sums`, which holds one entry per weight.
