class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        This function calculates how many contiguous subarrays of size 'k' 
        in the input array 'arr' have an average value greater than or equal 
        to a given 'threshold'.
        
        Parameters:
        arr (List[int]): The input array of integers.
        k (int): The size of the subarrays.
        threshold (int): The threshold value for the average of the subarray.
        
        Returns:
        int: The count of subarrays of size 'k' whose average is greater than
             or equal to the threshold.
        """
        
        # Initialize variables:
        # 'left' is the starting index of the sliding window.
        # 'window_sum' tracks the sum of the current window of size 'k'.
        # 'cnt' is the count of valid subarrays that meet the condition.
        # 'tgt' is the target sum, which is 'k * threshold', used to avoid division.
        left, window_sum, cnt, tgt = 0, 0, 0, k * threshold

        # Iterate over the array using the sliding window technique.
        for right, v in enumerate(arr):  # 'right' is the ending index of the window, 'v' is the value at index 'right'.
            
            # Add the current element to the window sum.
            window_sum += v
            
            # Calculate the size of the current window (it will be less than or equal to 'k').
            window_sz = right - left + 1
            
            # Once the window size reaches 'k', start evaluating the window.
            if window_sz == k:
                
                # Check if the sum of the window is greater than or equal to the target sum.
                # This avoids the need to compute the average.
                if window_sum >= tgt:
                    cnt += 1  # Increment the count if the condition is satisfied.
                
                # Slide the window by removing the left-most element and incrementing the 'left' pointer.
                window_sum -= arr[left]  # Subtract the element that is sliding out of the window.
                left += 1  # Move the left side of the window forward.

        # Return the total count of subarrays that meet the condition.
        return cnt
