class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        This function calculates the number of contiguous subarrays where the product of all the 
        elements is strictly less than `k`. It uses a sliding window approach to efficiently count 
        the valid subarrays.

        Parameters:
        nums (List[int]): A list of positive integers.
        k (int): The target product. We are counting subarrays whose product is strictly less than `k`.

        Returns:
        int: The number of subarrays whose product is less than `k`.

        Time Complexity: O(n), where `n` is the length of the input array `nums`. Both the `left` 
                         and `right` pointers traverse the array at most once, making the algorithm linear.
                         
        Space Complexity: O(1), because we only use a few extra variables (`left`, `prod`, and `cnt`) 
                          that do not grow with the size of the input.
        """

        # `left` is the left boundary of the sliding window.
        # `prod` stores the product of the current subarray.
        # `cnt` will store the number of valid subarrays.
        left, prod, cnt = 0, 1, 0

        # Traverse the array using `right` as the right boundary of the sliding window.
        for right in range(len(nums)):
            # Multiply the current element `nums[right]` to the product of the current window.
            prod *= nums[right]

            # If the product of the current window is greater than or equal to `k`, 
            # shrink the window from the left by dividing `prod` by `nums[left]` and incrementing `left`.
            while left <= right and prod >= k:
                prod //= nums[left]  # Remove the left-most element from the product.
                left += 1  # Move the left boundary to the right.

            # At this point, `prod < k`, so all subarrays ending at `right` are valid.
            # The number of valid subarrays ending at `right` is `(right - left + 1)` because every 
            # subarray starting from any index between `left` and `right` is valid.
            cnt += (right - left + 1)

        # Return the total count of valid subarrays.
        return cnt
