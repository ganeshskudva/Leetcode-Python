class Solution:
    def minimumSize(self, nums, max_operations):
        # Helper function to check feasibility for a given `mid` as the max bag size.
        # Returns True if we can divide all numbers with at most `max_operations`.
        def canDivide(mid):
            # `(num - 1) // mid` calculates the required operations for each number
            # to reduce it to parts not exceeding `mid`. Avoids floating-point math.
            return sum((num - 1) // mid for num in nums) <= max_operations

        # Initialize binary search bounds
        low, high = 1, max(nums)  # Smallest size is 1; largest size is the largest element in `nums`.

        # Binary search to find the minimum possible maximum bag size
        while low < high:
            mid = (low + high) // 2  # Find the mid-point

            # If `mid` is a feasible max size, search in the lower half
            if canDivide(mid):
                high = mid
            else:
                # Otherwise, search in the upper half
                low = mid + 1

        # Return the minimum size of the largest bag
        return low

# Time Complexity:
# 1. Binary Search:
#    - The binary search operates on the range [1, max(nums)].
#    - The number of iterations is approximately O(log(max(nums))).
# 2. Feasibility Check (canDivide):
#    - For each value of `mid`, canDivide iterates through the array `nums`, 
#      which has `n` elements. This operation is O(n).
# 3. Total Complexity:
#    - The binary search calls canDivide at most O(log(max(nums))) times.
#    - Each call to canDivide is O(n).
#    - Thus, the overall time complexity is O(n * log(max(nums))).

# Space Complexity:
# 1. The algorithm operates in-place and does not use additional data structures.
# 2. The helper function `canDivide` uses constant space O(1) for its calculations.
# 3. Therefore, the total space complexity is O(1).

# Summary:
# Time Complexity: O(n * log(max(nums)))
# Space Complexity: O(1)
