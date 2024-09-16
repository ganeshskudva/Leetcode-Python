class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sort the array to ensure we can work on increasing values, making it easier
        # to accumulate values by adding to the smaller ones to reach the larger ones.
        nums.sort()
        
        # Initialize pointers and variables:
        # i is the left pointer for the sliding window.
        # n is the length of the nums array.
        # res stores the maximum frequency of any number we can achieve.
        # tot keeps track of the total sum of the current window (sum of numbers from i to j).
        i, n, res, tot = 0, len(nums), 1, 0
        
        # Iterate through the array with the j pointer (right boundary of the window)
        for j in range(n):
            # Add the current number (nums[j]) to the total sum of the window.
            tot += nums[j]
            
            # While the current window is not valid (i.e., it requires more than k operations to make
            # all elements in the window equal to nums[j]), shrink the window from the left (increment i).
            while (j - i + 1) * nums[j] - tot > k:
                # Subtract the leftmost element from the total sum, as we are excluding it from the window.
                tot -= nums[i]
                # Move the left pointer to the right to shrink the window.
                i += 1
            
            # Update the result with the maximum window size found so far.
            res = max(res, j - i + 1)
        
        # Return the maximum frequency found.
        return res