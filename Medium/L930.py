# Prefix Sum + HashMap
from collections import defaultdict
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Find the number of subarrays with a sum equal to the given goal.

        Args:
        nums (List[int]): Binary array of 0s and 1s.
        goal (int): Target sum.

        Returns:
        int: Number of subarrays with sum equal to the goal.

        Time Complexity: O(n), where n is the size of the input array.
            - We iterate through the array once, and dictionary operations (insert and lookup) are O(1) on average.

        Space Complexity: O(n), where n is the size of the input array.
            - In the worst case, the hash map stores up to n different prefix sums.
        """
        count = 0  # To store the number of valid subarrays
        current_sum = 0  # Tracks the cumulative sum of elements
        prefix_sums = defaultdict(int)  # Stores the frequency of prefix sums
        prefix_sums[0] = 1  # Base case: to handle subarrays starting from index 0

        for num in nums:
            current_sum += num  # Update cumulative sum
            # If (current_sum - goal) exists in prefix_sums, add its frequency to count
            count += prefix_sums[current_sum - goal]
            # Increment the frequency of the current_sum in prefix_sums
            prefix_sums[current_sum] += 1

        return count

# Time Complexity: O(n), where n is the size of the input array.
# Space Complexity: O(n), where n is the size of the input array.


# SLiding Window
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        This function calculates the number of subarrays whose sum is exactly equal to `goal`.
        It uses a sliding window technique to first compute the number of subarrays with sums 
        at most equal to `goal` and then subtracts the number of subarrays with sums at most 
        equal to `goal - 1` to get the number of subarrays with sums exactly equal to `goal`.

        Parameters:
        nums (List[int]): A list of integers consisting only of 0s and 1s.
        goal (int): The target sum for the subarrays.

        Returns:
        int: The number of subarrays whose sum is exactly equal to `goal`.
        """

        def at_most(tgt):
            """
            This helper function calculates the number of subarrays whose sum is at most `tgt`.
            
            Parameters:
            tgt (int): The target sum for the subarrays.

            Returns:
            int: The number of subarrays whose sum is at most `tgt`.

            Time Complexity: O(n), where `n` is the length of `nums`. The sliding window ensures that 
                             the `left` pointer moves as necessary, and the `right` pointer iterates 
                             through each element exactly once, making this part of the solution linear.

            Space Complexity: O(1), since only a few variables (`left`, `res`, `tgt`) are used, 
                              regardless of the input size.
            """
            # If the target is negative, no valid subarrays can exist, so return 0.
            if tgt < 0:
                return 0

            # Initialize pointers and result variable:
            # `left` is the left boundary of the sliding window.
            # `res` will store the number of valid subarrays.
            left, res = 0, 0

            # Traverse the array using `right` as the right boundary of the sliding window.
            for right in range(len(nums)):
                # Subtract the current element from the target `tgt`.
                tgt -= nums[right]

                # If `tgt` becomes negative, we need to shrink the window by moving `left` to the right.
                while tgt < 0:
                    tgt += nums[left]  # Add back the element at `nums[left]` to restore the target sum.
                    left += 1          # Move the left boundary to the right.

                # Add the number of valid subarrays ending at `right` to the result.
                # The number of subarrays that end at `right` is `(right - left + 1)`.
                # This is because for each valid `right` position, all subarrays between `left` and `right`
                # are valid and have a sum ≤ `tgt`.
                res += (right - left + 1)

            return res

        # The final result is the number of subarrays whose sum is exactly equal to `goal`.
        # This is calculated as the number of subarrays with sum at most `goal` minus the number of subarrays
        # with sum at most `goal - 1`.
        return at_most(goal) - at_most(goal - 1)

# Time Complexity: O(n), where `n` is the length of `nums`. The sliding window ensures that 
#                  both the `left` and `right` pointers traverse the array at most once, 
#                  leading to a linear time complexity.
                 
# Space Complexity: O(1), as the solution only uses a few variables (`left`, `res`, `tgt`) 
#                   that do not depend on the size of the input.