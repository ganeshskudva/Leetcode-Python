class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Define a closure to encapsulate the logic for recursive function 'f'
        def solve():
            n = len(nums)
            max_or = reduce(or_, nums)  # Calculate the maximum OR possible
            dp = [[-1 for _ in range(max_or + 1)] for _ in range(n)]

            # Inner recursive function to compute number of subsets that achieve max_or
            def recurse(i, acc_or):
                if i < 0:
                    # Base case: return 1 if accumulated OR equals max_or
                    return 1 if acc_or == max_or else 0
                if dp[i][acc_or] != -1:
                    # Memoized case: return the stored result
                    return dp[i][acc_or]
                # Recur by skipping the current element
                skip = recurse(i - 1, acc_or)
                # Recur by including the current element and updating OR
                take = recurse(i - 1, acc_or | nums[i])
                # Store the result in dp array for future lookups
                dp[i][acc_or] = skip + take
                return dp[i][acc_or]

            # Initial call to the recursive function
            return recurse(n - 1, 0)

        # Execute the closure and return the result
        return solve()


# Time Complexity (TC): 
# The recursive function visits each subset of the nums array. 
# It takes O(2^n) where 'n' is the length of nums, because every element can either be included or excluded.
# The memoization reduces the number of redundant calculations. Hence, the effective time complexity is O(n * max_OR).

# Space Complexity (SC): 
# We use a DP table of size O(n * max_OR), where 'n' is the size of nums and max_OR is the maximum OR value.
# The space complexity is O(n * max_OR).