from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Handle edge cases where no average computation is needed
        if k == 0:
            return nums
        if len(nums) < 2 * k + 1:
            return [-1] * len(nums)
        
        # Initialize result array with -1, as we can't compute averages for indices that are out of bounds.
        res = [-1] * len(nums)
        
        # Initialize sliding window variables
        left, curWindowSum, diameter = 0, 0, 2 * k + 1
        
        # Traverse through the nums array with a sliding window approach
        for right in range(len(nums)):
            # Add current element to the current window sum
            curWindowSum += nums[right]
            
            # Check if window has reached required diameter (2k+1)
            if (right - left + 1 >= diameter):
                # Calculate and store the average for the middle element of the current window
                res[left + k] = curWindowSum // diameter
                # Remove the leftmost element from the window sum and move the window forward
                curWindowSum -= nums[left]
                left += 1
        
        return res

# Time Complexity (TC): O(n)
# - We iterate through the nums array only once using a sliding window, 
#   adding and removing elements from the window sum. Each element is processed in constant time, 
#   resulting in an overall time complexity of O(n), where n is the length of nums.

# Space Complexity (SC): O(n)
# - We use an additional array, res, of the same length as nums to store the results, 
#   which requires O(n) space. There is no other significant additional space usage.
