from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)  # Length of the nums array
        freq = [0] * (n + 1)  # Extend the frequency array by 1 to avoid boundary checks

        # Process each query and update the frequency array
        for start, end in queries:
            freq[start] += 1  # Increment the effect at the start index
            freq[end + 1] -= 1  # Decrement the effect right after the end index
        
        # Accumulate the frequency to check if the current state satisfies nums
        curr = 0  # Variable to store the running sum of the frequencies
        for i in range(n):
            curr += freq[i]  # Update the cumulative effect at index i
            if curr < nums[i]:  # If the cumulative effect is less than nums[i], return False
                return False  # This means the condition of making nums[i] zero cannot be satisfied

        # If the loop completes without returning False, the array can be made zero
        return True

# Time Complexity (TC):
# 1. Initializing the frequency array (`freq`): O(n), where n is the length of the nums array.
# 2. Processing the queries: O(q), where q is the number of queries.
#    - For each query, two constant-time updates are made to the frequency array.
# 3. Validating the nums array: O(n), iterating through the nums and cumulative frequency arrays.
# Overall TC: O(n + q).

# Space Complexity (SC):
# 1. Frequency array (`freq`): O(n + 1), to account for the extended size to avoid boundary checks.
# 2. Additional variables (`curr`): O(1), constant space.
# Overall SC: O(n).
