from typing import List
import math

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Set a large constant for an unachievable maximum distance
        maxi = int(1e16)
        
        # Sort robots and factories by position to allow pairing them in order
        # Time Complexity: O(r log r + f log f), where r is the number of robots and f is the number of factories
        robot.sort()
        factory.sort()

        # Flatten the factory list to create a list `v` where each position appears according to its capacity
        # Space Complexity: O(total capacity of all factories)
        v = []
        for position, capacity in factory:
            v.extend([position] * capacity)

        # Initialize a 2D DP table to memoize the minimum distance for each robot-factory pairing
        # dp[i][j] will store the minimum distance for robot `i` starting from factory position `j`
        # Space Complexity: O(r * f), where r is the number of robots and f is the total capacity of factories
        dp = [[-1] * (len(v) + 1) for _ in range(len(robot) + 1)]
        
        # Define the recursive helper function `f` with memoization using closure
        def f(i, j):
            # Base Case 1: If all robots have been paired
            if i == len(robot):
                return 0  # No additional distance needed
            
            # Base Case 2: If we have exhausted all factory positions but still have robots left
            if j == len(v):
                return maxi  # Unachievable large distance for invalid pairing
            
            # Return cached result if computed previously
            if dp[i][j] != -1:
                return dp[i][j]
            
            # Calculate distance by choosing to pair robot `i` with factory position `v[j]`
            take = abs(robot[i] - v[j]) + f(i + 1, j + 1)
            # Calculate distance by not pairing robot `i` with factory position `v[j]`
            not_take = f(i, j + 1)
            
            # Store and return the minimum distance in DP table
            dp[i][j] = min(take, not_take)
            return dp[i][j]

        # Start the recursive pairing from the first robot and the first factory position
        return f(0, 0)

# Overall Complexity Summary:
# Time Complexity: O(r * f), where r is the number of robots and f is the total capacity of all factories
#                  This is due to memoization with each subproblem evaluated once.
# Space Complexity: O(r * f) for the DP table to store results of subproblems.
#                   Additional O(r + f) space for sorted robots and flattened factory list.
