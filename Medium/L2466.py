# Top Down
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1000000007  # Modulo value to handle large numbers
        mp, res = {}, 0  # Memoization dictionary and result accumulator
        
        # Recursive function to calculate the number of good strings of a given target length
        def solve(target):
            if target == 0:  # Base case: one valid way to form a string of length 0
                return 1
            if target < 0:  # Base case: no valid way to form a string with negative length
                return 0
            if target in mp:  # Return the cached result if it exists
                return mp[target]
            
            # Recursively calculate the number of ways to form strings by adding `zero` or `one`
            mp[target] = (solve(target - one) + solve(target - zero)) % MOD
            return mp[target]
        
        # Iterate through each length from `low` to `high` and calculate the total count
        for i in range(low, high + 1):
            res = (res + solve(i)) % MOD  # Add the result for each length modulo MOD
        
        return res  # Return the final result

# Time Complexity (TC):
# O(n * m), where:
# - n = (high - low + 1), the range of lengths we need to calculate.
# - m = maximum value of `high`, as each target length uses memoization to avoid redundant computations.
# - Overall, the recursion depth depends on the maximum target value and the memoization ensures each value is computed only once.

# Space Complexity (SC):
# O(m), where:
# - m = maximum value of `high`, as the memoization dictionary `mp` stores results for each target length.
# - Additional stack space used in recursion is proportional to the target value, which is bounded by `high`.

# Bottom Up
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1000000007  # Modulo value to handle large numbers

        # Create a DP array to store the number of good strings for each length
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: one way to form a string of length 0

        # Fill the DP array iteratively
        for length in range(1, high + 1):
            # If we can use 'zero', add the ways from length - zero
            if length >= zero:
                dp[length] = (dp[length] + dp[length - zero]) % MOD
            # If we can use 'one', add the ways from length - one
            if length >= one:
                dp[length] = (dp[length] + dp[length - one]) % MOD

        # Sum up the results for lengths in the range [low, high]
        result = sum(dp[low:high + 1]) % MOD
        return result

# Time Complexity (TC):
# O(high):
# - Filling the DP array takes O(high) since we iterate through lengths from 1 to high.
# - Summing up the results for the range [low, high] takes O(high - low + 1), which is at most O(high).
# - Combined, the complexity remains O(high).

# Space Complexity (SC):
# O(high):
# - The DP array requires O(high + 1) space to store the number of ways for each length.
# - No additional data structures or recursion stacks are used, so the total space complexity is O(high).

