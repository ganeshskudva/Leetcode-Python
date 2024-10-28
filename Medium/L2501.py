from typing import List
from math import isqrt

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Use a set to store unique elements for efficient lookup
        st = set(nums)
        lss = -1  # Initialize the longest square streak (lss) to -1

        # Iterate over each number in nums to calculate the square streak
        for num in nums:
            # Start a new streak only if `sqrt(num)` is not in the set
            if isqrt(num) ** 2 != num or isqrt(num) not in st:
                css = 1  # Current square streak length
                a = num
                # Remove the starting element of the streak from the set
                st.discard(a)
                
                # Continue the streak as long as `a * a` exists in the set
                while a * a in st:
                    css += 1
                    st.discard(a * a)  # Remove `a * a` from the set to avoid reprocessing
                    a = a * a  # Update `a` to `a * a` to continue checking next in sequence
                
                # Update the longest streak length if the current streak is greater or equal to 2
                if css >= 2:
                    lss = max(lss, css)

        return lss  # Return the longest square streak

# Time Complexity (TC): O(n log k), where `n` is the length of `nums` and `k` is the maximum possible value in `nums`.
# - The outer loop iterates over each element in `nums` once.
# - For each element, the inner while loop performs log(k) operations in the worst case, as it squares `a` in each iteration.
# - Thus, the total time complexity is O(n log k).

# Space Complexity (SC): O(n)
# - The set `st` stores all unique elements from `nums`, which uses O(n) space in the worst case.
# - Additional space is minimal as only a few auxiliary variables are used.
