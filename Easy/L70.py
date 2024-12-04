# Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        # Memoization dictionary to store the results of subproblems
        # Base cases: 0 steps => 0 ways, 1 step => 1 way, 2 steps => 2 ways
        mp = {0: 0, 1: 1, 2: 2}

        # Recursive function to solve the problem
        def solve(n):
            # If the result for the current 'n' is already computed, return it
            if n in mp:
                return mp[n]

            # Recursive case: compute the number of ways for 'n' using the
            # sum of ways to reach (n-1) and (n-2) steps
            mp[n] = solve(n - 1) + solve(n - 2)
            return mp[n]

        # Initiate the computation with the given number of steps
        return solve(n)

# Time Complexity:
# Each step's value is computed at most once, and we store the result in `mp`.
# The recursion runs in O(n) as it calculates values for all steps from 1 to n.
#
# Space Complexity:
# Space is used for the recursion stack and the `mp` dictionary.
# - Recursion stack depth: O(n) in the worst case (linear recursion depth).
# - Dictionary `mp`: O(n) for storing results of all subproblems.
# Overall: O(n) space.

# Iterative
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Variables to store the last two results
        prev1 = 1  # Ways to climb 1 step
        prev2 = 2  # Ways to climb 2 steps

        # Iteratively calculate the number of ways to climb to the nth step
        for i in range(3, n + 1):
            current = prev1 + prev2  # Current step = sum of last two steps
            prev1 = prev2  # Update prev1 to the previous step
            prev2 = current  # Update prev2 to the current step

        return prev2  # Final result is stored in prev2

# Time Complexity:
# - The loop runs from 3 to n, i.e., O(n).
#
# Space Complexity:
# - We only use two variables (`prev1` and `prev2`) to store intermediate results.
# - Thus, the space complexity is O(1).
