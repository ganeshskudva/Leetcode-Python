from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate, missing = -1, -1

        # Use indices to mark visited numbers
        for num in nums:
            index = abs(num) - 1  # Convert to 0-based index
            if nums[index] < 0:
                # If already negative, it's the duplicate number
                duplicate = abs(num)
            else:
                # Mark the number as visited by negating it
                nums[index] = -nums[index]

        # Find the missing number by checking for positive values
        for i in range(n):
            if nums[i] > 0:
                # Missing number is the index + 1 (convert back to 1-based)
                missing = i + 1

        return [duplicate, missing]

# Time Complexity (TC): O(n)
# Explanation:
# - The first loop processes each number in nums, marking indices, which takes O(n).
# - The second loop checks for positive values to identify the missing number, which also takes O(n).
# - Total time complexity: O(n).

# Space Complexity (SC): O(1)
# Explanation:
# - The solution modifies the input array `nums` in-place to track visited numbers, requiring no additional data structures.
# - Total space complexity: O(1).
