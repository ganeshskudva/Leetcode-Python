# Top Down
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Memoization dictionary to store computed results
        mp = {}
        
        def solve(i, taken):
            # Base case: if we have already taken 2 elements, stop adding scores
            if taken >= 2:
                return 0
            
            # If we reach beyond the array, return negative infinity
            if i >= len(values):
                return -math.inf
            
            # Memoization check
            key = (i, taken)
            if key in mp:
                return mp[key]
            
            # Choice: either pick the current index or skip it
            pick, notPick = values[i] + solve(i + 1, taken + 1), solve(i + 1, taken)
            
            # Adjust score for the sightseeing pair condition
            if taken == 1:  # Second element chosen, subtract its index
                pick -= i
            else:  # First element chosen, add its index
                pick += i
            
            # Store the result in memoization dictionary
            mp[key] = max(pick, notPick)
            return mp[key]
        
        # Start the recursive function
        return solve(0, 0)

# Time Complexity (TC): O(n * 2)
# The memoization table can have at most n * 2 entries (n is the size of the input array),
# as there are n indices and at most two possible values for 'taken' (0 or 1).
# Each recursive call does O(1) work apart from the recursive calls.

# Space Complexity (SC): O(n * 2) for the memoization table + O(n) for the recursion stack.
# This is O(n) overall, as the recursion stack is limited to n depth and the memoization
# dictionary has O(n * 2) entries.

# Bottom Up
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Initialize variables
        max_so_far = values[0]  # Tracks the best "values[i] + i" seen so far
        max_score = float('-inf')  # Tracks the best sightseeing pair score

        for j in range(1, len(values)):
            # Update max_score using the current `values[j] - j` and the best seen so far
            max_score = max(max_score, max_so_far + values[j] - j)
            # Update max_so_far for the next iteration
            max_so_far = max(max_so_far, values[j] + j)
        
        return max_score

# Time Complexity (TC): O(n)
# We only traverse the array once, updating `max_so_far` and `max_score` at each step.

# Space Complexity (SC): O(1)
# No additional space is used apart from a few variables.
