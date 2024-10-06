class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        This function calculates the number of subarrays where the maximum element appears at least `k` times.
        It uses a sliding window approach to efficiently count such subarrays.

        Parameters:
        nums (List[int]): A list of integers.
        k (int): The minimum number of times the maximum element must appear in the subarray.

        Returns:
        int: The number of subarrays where the maximum element appears at least `k` times.

        Time Complexity: O(n), where `n` is the length of the input array `nums`. Both the `left` 
                         and `right` pointers traverse the array at most once, making the algorithm linear.
                         
        Space Complexity: O(1), as the solution uses only a few variables (`left`, `cnt`, `max_elem`, `res`) 
                          that do not depend on the size of the input.
        """

        # `left` is the left boundary of the sliding window.
        # `cnt` counts how many times the maximum element (`max_elem`) appears in the current window.
        # `max_elem` is the maximum element of the entire array `nums` (this remains constant throughout).
        # `res` stores the final result, which is the number of valid subarrays found.
        left, cnt, max_elem, res = 0, 0, max(nums), 0

        # Traverse the array using `right` as the right boundary of the sliding window.
        for right in range(len(nums)):
            # If the current element is the maximum element, increment `cnt`.
            if nums[right] == max_elem:
                cnt += 1

            # Shrink the window if `cnt` (number of `max_elem` in the window) is greater than or equal to `k`.
            # This ensures that the subarray meets the condition of having fewer than `k` occurrences of `max_elem`.
            while left <= right and cnt >= k:
                # If the element at `nums[left]` is the maximum element, decrement `cnt` since it's being removed.
                if nums[left] == max_elem:
                    cnt -= 1
                left += 1  # Move the left boundary to shrink the window.

            # Add `left` to the result `res`. For every valid `right` position, all subarrays that end at `right`
            # and start from any index before `left` (up to `right`) are valid.
            res += left

        # Return the total number of valid subarrays.
        return res
