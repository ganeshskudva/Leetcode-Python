class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        This function calculates the minimum number of operations required to reduce x to 0 by removing elements
        from the beginning or end of the list `nums`. Each operation involves removing one element from either end of the list.
        The problem can be translated into finding the longest subarray that sums to `total_sum - x`, 
        where `total_sum` is the sum of the entire array.

        Parameters:
        nums (List[int]): The input list of integers.
        x (int): The target value that we want to reduce to 0 by removing elements.

        Returns:
        int: The minimum number of operations to reduce `x` to 0. If it's not possible, return -1.
        """

        # `tot` is the total sum of all elements in `nums`.
        tot = sum(nums)

        # Initialize two pointers (`left` is the start of the sliding window).
        left = 0

        # `max_len` will store the length of the longest subarray that sums to `tot - x`. 
        # We initialize it to `float('-inf')` to represent that no valid subarray has been found initially.
        max_len = float('-inf')

        # `curr` will track the sum of the current sliding window.
        curr = 0

        # Iterate through the array using the `right` pointer.
        for right in range(len(nums)):
            # Add the current element `nums[right]` to the current window sum `curr`.
            curr += nums[right]

            # If the current sum `curr` exceeds the target sum (`tot - x`), shrink the window by moving `left` to the right.
            while left <= right and curr > tot - x:
                curr -= nums[left]  # Remove the element at `nums[left]` from `curr`.
                left += 1  # Move the `left` boundary to the right.

            # If the current window sum `curr` is exactly equal to `tot - x`, we update `max_len`.
            if curr == tot - x:
                max_len = max(max_len, right - left + 1)

        # If no valid subarray was found (`max_len` is still `float('-inf')`), return -1.
        # Otherwise, return the minimum number of operations, which is the total array length minus the length of the found subarray.
        return -1 if max_len == float('-inf') else len(nums) - max_len
