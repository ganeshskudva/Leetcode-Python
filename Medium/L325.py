from typing import List
from collections import defaultdict

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Return 0 immediately if nums is empty
        if not nums:
            return 0
        
        # Initialize a dictionary to store cumulative sums and their first occurrence index
        mp = defaultdict(int)
        # `tot` is the running total of the cumulative sum, `max_len` stores the maximum subarray length found
        tot, max_len = 0, float('-inf')
        # Store cumulative sum of 0 at index -1 to handle cases where a subarray starting from index 0 meets the target sum
        mp[0] = -1

        # Traverse each element in nums
        for i in range(len(nums)):
            # Update the cumulative sum up to the current index
            tot += nums[i]
            # Calculate the target (tgt) cumulative sum we need for a valid subarray
            tgt = tot - k
            
            # Check if tgt has been seen before in mp
            # If it has, we have found a subarray ending at index `i` with sum `k`
            if tgt in mp:
                # Update max_len if the new subarray is longer than previously found ones
                max_len = max(max_len, i - mp[tgt])
            
            # Only store the cumulative sum `tot` if it has not been seen before,
            # to ensure we store the earliest occurrence of each cumulative sum
            if tot not in mp:
                mp[tot] = i

        # If no valid subarray was found, return 0; otherwise, return the length of the longest subarray found
        return 0 if max_len == float('-inf') else max_len

# Time Complexity (TC):
# - The main loop iterates through each element in `nums`, taking O(N) time where N is the length of `nums`.
# - All dictionary operations (insertions and lookups) are O(1) on average.
# - Overall time complexity: O(N).

# Space Complexity (SC):
# - We store cumulative sums in the dictionary `mp`, which in the worst case could hold up to N unique sums.
# - Therefore, the space complexity is O(N).
