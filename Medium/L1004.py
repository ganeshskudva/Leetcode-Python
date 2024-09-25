class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0  # Initialize two pointers, left and right, to track the window boundaries
        for right in range(len(nums)):  # Iterate through the list with the right pointer
            if nums[right] == 0:  # If the current number is 0, we decrement the allowed flips (k)
                k -= 1
            if k < 0:  # If k becomes negative, it means we have used more than the allowed flips
                if nums[left] == 0:  # Move the left pointer to shrink the window
                    k += 1  # If nums[left] was 0, increase k because we're "reclaiming" a flip
                left += 1  # Move the left pointer to the right to maintain a valid window

        return right - left + 1  # Return the length of the largest valid window