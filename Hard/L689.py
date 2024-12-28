class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)

        # Precompute prefix sums for efficient range sum calculation
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        # Helper function to compute the sum of a subarray using prefix sums
        def subarray_sum(start, length):
            return prefix_sums[start + length] - prefix_sums[start]

        # Best indices for single, double, and triple subarrays
        best_one, best_two, best_three = 0, [0, k], [0, k, 2 * k]
        best_one_sum = subarray_sum(0, k)
        best_two_sum = subarray_sum(0, k) + subarray_sum(k, k)
        best_three_sum = (
            subarray_sum(0, k) + subarray_sum(k, k) + subarray_sum(2 * k, k)
        )

        for i in range(1, n - 3 * k + 1):
            # Update the best single subarray
            one_sum = subarray_sum(i, k)
            if one_sum > best_one_sum:
                best_one = i
                best_one_sum = one_sum

            # Update the best two subarrays
            two_sum = best_one_sum + subarray_sum(i + k, k)
            if two_sum > best_two_sum:
                best_two = [best_one, i + k]
                best_two_sum = two_sum

            # Update the best three subarrays
            three_sum = best_two_sum + subarray_sum(i + 2 * k, k)
            if three_sum > best_three_sum:
                best_three = best_two + [i + 2 * k]
                best_three_sum = three_sum

        return best_three

# Time Complexity (TC):
# O(n), where n is the length of the input list `nums`.
# - Precomputing the prefix sums takes O(n).
# - The loop that identifies the best subarrays iterates through the array once.

# Space Complexity (SC):
# O(n), due to the prefix sums array.
# - The prefix sums array requires O(n) space.
# - Other variables (best_one, best_two, best_three) use O(1) space, so the total space complexity is dominated by the prefix sums.
