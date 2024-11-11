class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Initialize the result array with -1, where res[i] will store
        # the average if it's possible to calculate it, otherwise remain -1
        res = [-1] * len(nums)
        
        # Initialize variables:
        # `left` - starting index of the sliding window
        # `curWindowSum` - sum of the current window of size `diameter`
        # `diameter` - total elements in the window, i.e., 2*k+1
        left, curWindowSum, diameter = 0, 0, 2 * k + 1
        
        # Loop through each index `right`, which will serve as the end of the sliding window
        for right in range(len(nums)):
            # Add the current number at `right` to the current window sum
            curWindowSum += nums[right]
            
            # Check if the window has reached the required size (2*k+1)
            if (right - left + 1 >= diameter):
                # Calculate the average of the current window and assign it to the middle index
                res[left + k] = curWindowSum // diameter
                
                # Slide the window forward:
                # Subtract the element at `left` from the window sum and increment `left`
                curWindowSum -= nums[left]
                left += 1
        
        # Return the final result array with averages and -1 for non-calculable positions
        return res

# Time Complexity (TC): O(N), where N is the number of elements in `nums`.
# - We iterate through `nums` exactly once, maintaining a sliding window, which makes each operation O(1).

# Space Complexity (SC): O(N), where N is the number of elements in `nums`.
# - We use an additional list `res` of the same length as `nums` to store the output.
