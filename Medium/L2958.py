from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        This function calculates the length of the longest subarray where no number appears 
        more than `k` times. It uses a sliding window approach to efficiently count the length 
        of valid subarrays.

        Parameters:
        nums (List[int]): A list of integers.
        k (int): The maximum allowed occurrences of any number in the subarray.

        Returns:
        int: The length of the longest subarray where no number appears more than `k` times.

        Time Complexity: O(n), where `n` is the length of the input array `nums`. The sliding window 
                         ensures that both the `left` and `right` pointers traverse the array at most once, 
                         making the algorithm linear.

        Space Complexity: O(m), where `m` is the number of unique elements in `nums`. The dictionary 
                          `mp` keeps track of the count of each number within the current window, so 
                          the space complexity depends on the number of unique numbers.
        """

        # Early return for edge cases.
        if k == 0:
            return 0  # No valid subarray can exist if k is 0.

        # `left` is the left boundary of the sliding window.
        # `max_len` stores the maximum length of a valid subarray found so far.
        # `mp` is a dictionary that keeps track of the frequency of each number in the current window.
        left, max_len = 0, 0
        mp = defaultdict(int)  # A dictionary to count occurrences of numbers in the window.

        # Traverse the array using `right` as the right boundary of the sliding window.
        for right in range(len(nums)):
            # Increment the count of the current element `nums[right]` in the frequency map.
            mp[nums[right]] += 1

            # If the frequency of `nums[right]` exceeds `k`, shrink the window from the left.
            while left <= right and mp[nums[right]] > k:
                mp[nums[left]] -= 1  # Decrement the count of `nums[left]` as it leaves the window.
                left += 1  # Move the left boundary to the right.

            # Update `max_len` to the maximum length of any valid subarray found so far.
            max_len = max(max_len, right - left + 1)

        # Return the maximum length of a valid subarray found.
        return max_len
