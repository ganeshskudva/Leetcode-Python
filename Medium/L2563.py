class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        # Helper function to count pairs with sums less than or equal to `t`
        def count(t):
            i, j = 0, len(nums) - 1
            res = 0
            
            # Two-pointer approach to find all pairs with sum <= t
            while i < j:
                if nums[i] + nums[j] > t:
                    j -= 1  # Move `j` left to reduce the sum
                else:
                    res += j - i  # Count all pairs (i, i+1), ..., (i, j)
                    i += 1       # Move `i` right to explore next possible pairs
            
            return res

        # Sort the array to use two-pointer technique effectively
        nums.sort()

        # Calculate the number of pairs with sum in range [lower, upper]
        return count(upper) - count(lower - 1)

# Time Complexity (TC): O(n log n) due to sorting the array, where `n` is the length of `nums`.
# The count function itself is O(n) as it makes a single pass through `nums` with two pointers.
# So the overall complexity is O(n log n).

# Space Complexity (SC): O(1) excluding the input array, as only a constant amount of additional space
# is used. Sorting modifies the input array in-place, so no extra space is required for sorting.
