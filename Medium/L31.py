from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to the next lexicographical permutation of the numbers.
        If such arrangement is not possible, it rearranges it to the lowest possible order.
        """
        # Step 1: Find the first decreasing element from the right
        # Start from the second last element and move left
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1  # Continue moving left until a smaller element is found

        # Step 2: If such an element is found, find the next larger element to swap with
        if i >= 0:  # Only proceed if a decreasing element was found
            j = len(nums) - 1  # Start from the last element
            while nums[j] <= nums[i]:  # Find the smallest element larger than nums[i]
                j -= 1
            # Swap the two elements to form the next permutation
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the elements after index i to get the next permutation
        # This step ensures the remaining part of the array is in the smallest possible order
        nums[i + 1:] = reversed(nums[i + 1:])

# Time Complexity (TC):
# 1. Finding the first decreasing element:
#    - In the worst case, we traverse the entire array, O(n), where n is the length of the array.
# 2. Finding the next larger element:
#    - In the worst case, we traverse the array from the rightmost element, O(n).
# 3. Reversing the subarray:
#    - In the worst case, we reverse a portion of the array, O(n).
# Overall TC: O(n), as the array is traversed a constant number of times.

# Space Complexity (SC):
# 1. The algorithm modifies the array in place without using extra space.
# 2. The reversal operation does not require additional space as it operates directly on the input array.
# Overall SC: O(1), since no additional data structures are used.
