from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Memoization dictionary to store results of subproblems
        mp = {}

        # Helper function to solve the problem recursively with memoization
        def solve(n):
            # Base case: if n is out of bounds, return 0 (no more houses to rob)
            if n >= len(nums):
                return 0
            # Check if the result for this house index n is already computed
            if n in mp:
                return mp[n]

            # Option 1: Rob this house and skip the next one (move to n + 2)
            take = nums[n] + solve(n + 2)
            # Option 2: Skip this house and move to the next house (n + 1)
            dontTake = solve(n + 1)

            # Store the maximum amount we can rob from house n in memoization dictionary
            mp[n] = max(take, dontTake)

            return mp[n]

        # Start solving from the first house
        return solve(0)

# Time Complexity (TC): O(n)
#   - The recursive function `solve` is called once for each index (0 to len(nums) - 1).
#   - Memoization ensures each index is computed only once, leading to O(n) time complexity.

# Space Complexity (SC): O(n)
#   - The memoization dictionary `mp` stores one result per index, leading to O(n) space.
#   - The recursion depth in the call stack also goes up to O(n), so total space complexity is O(n).
