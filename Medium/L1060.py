from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Initialize pointers for binary search
        left = 0
        right = len(nums) - 1

        # Perform binary search to locate the range where the k-th missing number lies
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle index
            # Calculate the number of missing elements from nums[0] to nums[mid]
            number_of_missing = nums[mid] - nums[0] - mid

            if k > number_of_missing:
                # If k is greater than the missing count at nums[mid], search the right half
                left = mid + 1
            else:
                # Otherwise, search the left half
                right = mid - 1

        # After the loop, left points to the smallest index where the k-th missing number is located

        # Calculate the number of missing elements up to nums[left - 1]
        number_of_missing = nums[left - 1] - nums[0] - (left - 1)

        # Calculate and return the k-th missing element
        # Add the remaining difference to nums[left - 1] to get the k-th missing number
        return nums[left - 1] + (k - number_of_missing)

# Time Complexity (TC):
# - The algorithm uses binary search, which halves the search space in each iteration.
# - The number of iterations is O(log n), where n is the length of the input array `nums`.
# - Calculating the missing count (`number_of_missing`) in each iteration is O(1).
# - Overall, the time complexity is O(log n).

# Space Complexity (SC):
# - The algorithm uses a constant amount of extra space for variables like `left`, `right`, `mid`, and `number_of_missing`.
# - No additional data structures or recursion are used.
# - Overall, the space complexity is O(1).
