class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Initialize variables:
        # 'cur' will track the length of the current subarray containing the maximum element
        # 'cur_max' keeps track of the maximum element found so far in the array
        # 'res' will store the length of the longest subarray found
        cur, cur_max, res = 0, 0, 0
        
        # Iterate through each element in the array 'nums'
        for i in nums:
            # If the current element 'i' is greater than the current maximum value 'cur_max'
            if i > cur_max:
                # Update 'cur_max' to the new maximum value 'i'
                # Reset the current subarray length 'cur' to 1 (since it's a new subarray with the new maximum)
                # Reset 'res' to 1 as the longest subarray with the new maximum starts here
                cur_max, cur, res = i, 1, 1
            
            # If the current element 'i' is equal to the current maximum 'cur_max'
            elif i == cur_max:
                # Increment 'cur' to extend the current subarray since 'i' is part of the max element subarray
                cur += 1
            
            # If the current element 'i' is less than 'cur_max'
            else:
                # Reset 'cur' to 0 because this breaks the subarray of maximum elements
                cur = 0
            
            # Update 'res' to be the maximum between 'res' and 'cur', ensuring 'res' always stores
            # the longest subarray of maximum elements found so far
            res = max(res, cur)
        
        # Return the final result, which is the length of the longest subarray of the maximum element
        return res
