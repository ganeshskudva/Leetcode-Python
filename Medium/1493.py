class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Initialize two pointers i and j to form a sliding window, and n is the length of nums.
        i, j, n, cnt = 0, 0, len(nums), 0  # 'cnt' counts the number of zeros in the current window.
        
        # Iterate through the array using the right pointer 'j'.
        for j in range(n):
            # If the current element is 0, increment the zero count 'cnt'.
            cnt += 1 if nums[j] == 0 else 0
            
            # If there are more than one zero in the window, we need to shrink the window from the left (i).
            if cnt > 1:
                # If the element at 'i' is a zero, decrement the count as we will remove it from the window.
                cnt -= 1 if nums[i] == 0 else 0
                # Move the left pointer 'i' to the right to shrink the window.
                i += 1
        
        # The length of the longest subarray with at most one zero is j - i.
        # We return j - i because we want the longest subarray where we can remove one zero.
        return j - i
