class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Helper function to check if a given `val` can distribute the quantities
        # such that no store gets more than `val` items, using at most `n` stores.
        def is_feasible(val):
            # Calculate the total number of stores needed if the maximum items
            # per store is limited to `val`. Use ceiling division with:
            # (num + val - 1) // val to avoid floating-point division.
            return sum((num + val - 1) // val for num in quantities) > n
        
        # Binary search range: minimum value is 1 (at least 1 item per store),
        # and the maximum value is the largest quantity in the array.
        left, right = 1, max(quantities)
        
        # Perform binary search to find the minimized maximum value
        while left < right:
            mid = left + (right - left) // 2  # Calculate the middle point
            
            # If `mid` is not feasible, increase `left` to search higher values
            if is_feasible(mid):
                left = mid + 1
            else:
                # If feasible, search lower values to minimize the maximum
                right = mid
        
        # `left` now holds the minimized maximum value
        return left

# Time Complexity (TC):
# - The binary search runs O(log(max(quantities))) iterations.
# - For each iteration, the `is_feasible` function iterates over the `quantities` array, taking O(m) time where `m` is the number of elements in `quantities`.
# - Overall, TC = O(m * log(max(quantities))).

# Space Complexity (SC):
# - The algorithm uses O(1) additional space since it only uses a few variables for computation.
# - SC = O(1).
