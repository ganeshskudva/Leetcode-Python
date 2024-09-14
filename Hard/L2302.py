class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize the left and right pointers of the sliding window
        l, r = 0, 0
        
        # Result to store the number of valid subarrays
        res = 0
        
        # Length of the input array
        m = len(nums)
        
        # Variable to store the current sum of the window (subarray)
        cur = 0
        
        # Iterate through the array with the right pointer 'r'
        while r < m:
            # Expand the window by including nums[r] in the current sum
            cur += nums[r]
            
            # Check if the product of the current sum and the length of the subarray is less than 'k'
            if cur * (r - l + 1) < k:
                # If valid, add the number of subarrays ending at 'r' and starting anywhere from 'l' to 'r'
                res += (r - l + 1)
            
            # If the current window's sum and length product is greater than or equal to 'k', shrink the window
            while cur * (r - l + 1) >= k:
                # Subtract nums[l] from the current sum to shrink the window from the left
                cur -= nums[l]
                # Move the left pointer to the right
                l += 1
                # After shrinking, check again if the new window is valid
                if cur * (r - l + 1) < k:
                    res += (r - l + 1)
            
            # Move the right pointer to expand the window
            r += 1
        
        # Return the total number of valid subarrays
        return res
