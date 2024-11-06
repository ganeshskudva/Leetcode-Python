class Solution:
    def canSortArray(self, nums):
        # If the array has only one element, it is trivially sorted
        if len(nums) == 1:
            return True

        def has_same_bit_count(a, b):
            # Helper function to check if two numbers have the same number of 1 bits in binary
            return bin(a).count('1') == bin(b).count('1')

        def is_sorted(nums):
            # Helper function to check if the array is sorted
            return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))

        # Start checking the array from the beginning
        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i + 1]:
                # Check if we can swap nums[i] and nums[i + 1] based on bit count
                if has_same_bit_count(nums[i], nums[i + 1]):
                    # Swap elements to move closer to sorted order
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    # Reset the index to re-check from the start after a swap
                    i = 0
                else:
                    # If we can't swap based on bit count, sorting is impossible
                    return False
            else:
                # Move to the next element if already in order
                i += 1

        # Final check to see if the array is sorted
        return is_sorted(nums)

# Time Complexity (TC):
# - Checking bit count (bin(a).count('1')) takes O(log a) for each pairwise comparison.
# - In the worst case, the algorithm rechecks the array after each swap, potentially up to O(n^2).
# - Overall: O(n * log(max(nums)) + n^2).

# Space Complexity (SC): O(1), as we use constant additional space for helper functions and a few variables.
