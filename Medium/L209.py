class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        This function finds the minimal length of a contiguous subarray of which the sum is at least `target`.
        If there is no such subarray, it returns 0.

        Parameters:
        target (int): The target sum we want to achieve or exceed.
        nums (List[int]): A list of positive integers.

        Returns:
        int: The minimal length of a contiguous subarray with a sum >= target. Returns 0 if no such subarray exists.
        """
        
        # Initialize variables:
        # `left` is the starting index of the sliding window.
        # `tot` keeps track of the sum of the current window.
        # `min_len` stores the minimum length of the subarray found so far.
        left, tot, min_len = 0, 0, float('inf')

        # Iterate through the array using `right` as the right boundary of the sliding window.
        for right in range(len(nums)):
            # Add the current element `nums[right]` to the total sum of the current window.
            tot += nums[right]
            
            # If the sum of the current window is greater than or equal to the target, try to shrink the window.
            while tot >= target:
                # Calculate the size of the current window.
                win_sz = right - left + 1
                
                # Update `min_len` to the smaller of the current `min_len` and the size of the current window.
                min_len = min(min_len, win_sz)
                
                # Shrink the window from the left side by subtracting `nums[left]` from the total.
                tot -= nums[left]
                
                # Move the left boundary of the window to the right.
                left += 1
        
        # If no valid subarray was found (i.e., `min_len` was not updated), return 0.
        # Otherwise, return the minimum length found.
        return 0 if min_len == float('inf') else min_len
