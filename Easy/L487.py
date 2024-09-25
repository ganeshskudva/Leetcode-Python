class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, k, mx = 0, 1, float('-inf')  # Initialize left pointer for the window, k for allowed flips (1 flip allowed), and mx for max length
        
        for right in range(len(nums)):  # Iterate over nums with the right pointer
            if nums[right] == 0:  # If the current element is 0, decrement k (using one flip)
                k -= 1
            if k < 0:  # If k goes negative, it means we've exceeded the allowed number of flips
                if nums[left] == 0:  # If the left element is 0, increment k back (reclaim the flip as we move left)
                    k += 1
                left += 1  # Move the left pointer to shrink the window

            mx = max(mx, right - left + 1)  # Update the maximum window size that can have at most one 0

        return 0 if mx == float('-inf') else mx  # If no valid window was found, return 0, otherwise return the maximum length
