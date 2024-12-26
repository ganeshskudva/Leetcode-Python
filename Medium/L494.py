class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Dictionary to store memoized results
        dp = {}
        
        def solve(idx, curr_sum=0):
            # Base case: If we've processed all numbers
            if idx < 0:
                # Check if the current sum matches the target
                if curr_sum == target:
                    return 1
                return 0
            
            # Create a unique key for the current state
            key = (idx, curr_sum)
            # If the result is already calculated, return it
            if key in dp:
                return dp[key]
            
            # Recursive case: Add or subtract the current number and move to the next index
            dp[key] = solve(idx - 1, curr_sum + nums[idx]) + solve(idx - 1, curr_sum - nums[idx])
            return dp[key]
        
        return solve(len(nums) - 1)

# Time Complexity (TC):
# Let n be the length of nums.
# Each state (idx, curr_sum) is calculated only once due to memoization.
# There are O(n * range_of_sums) states, where range_of_sums depends on the sum of all elements in nums.
# If the sum of elements is S, the total possible range of curr_sum is from -S to S, which is 2S+1.
# Therefore, TC = O(n * S).

# Space Complexity (SC):
# Space is used for the memoization dictionary dp and the recursive call stack.
# The size of dp is O(n * S) (number of unique states).
# The maximum depth of the recursive call stack is O(n).
# Total SC = O(n * S) for dp + O(n) for recursion stack.
