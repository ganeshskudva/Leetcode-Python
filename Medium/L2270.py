class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Calculate the total sum of the array
        total_sum = sum(nums)  # O(n)
        left_sum = 0
        valid_splits = 0

        # Iterate through the array except the last element
        for i in range(len(nums) - 1):
            left_sum += nums[i]            # Update the left sum
            right_sum = total_sum - left_sum  # Calculate the right sum dynamically
            
            if left_sum >= right_sum:       # Check the condition for a valid split
                valid_splits += 1

        return valid_splits

# Time Complexity (TC):
# O(n) - The array is traversed twice: once for calculating the total sum and once for evaluating valid splits.
# Space Complexity (SC):
# O(1) - Only a constant amount of extra space is used, as no additional data structures are required.