# Memoization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Initialize a defaultdict to store intermediate results (memoization)
        mp = defaultdict(int)
        
        # Recursive function to solve the problem
        def solve(n):
            # Base case: No cost for steps below 0
            if n < 0:
                return 0
            # Base case: Return the cost for the first two steps
            if n == 0 or n == 1:
                return cost[n]
            # If the value is already computed, return it from the memoization map
            if n in mp:
                return mp[n]
            # Recursive relation: Cost for the current step + minimum of the two previous steps
            mp[n] = cost[n] + min(solve(n - 1), solve(n - 2))
            return mp[n]
        
        # Calculate the minimum cost to reach the top
        return min(solve(len(cost) - 1), solve(len(cost) - 2))

# Time Complexity (TC): O(n)
#   - Each step is computed at most once due to memoization.
#   - Recursive calls are reduced to linear time, O(n), where n is the length of the cost array.

# Space Complexity (SC): O(n)
#   - Recursive call stack depth is proportional to the size of the input, which is O(n).
#   - Additional space is used for the memoization dictionary (mp), which also scales linearly with O(n).

# iterative
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Initialize variables to store the minimum cost for the last two steps
        prev2, prev1 = 0, 0  # Cost to step -2 and step -1
        
        # Compute the cost iteratively
        for c in cost:
            current = c + min(prev1, prev2)  # Current cost = cost of this step + min(previous two)
            prev2, prev1 = prev1, current  # Update for the next iteration
        
        # Return the minimum cost to reach the top
        return min(prev1, prev2)

# Time Complexity (TC): O(n)
#   - Single loop iterating through the cost array, linear in the size of the array.

# Space Complexity (SC): O(1)
#   - Constant space usage, only storing the last two costs (`prev2` and `prev1`).
