class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the array that sum up to zero.

        Parameters:
        nums (List[int]): Input list of integers.

        Returns:
        List[List[int]]: A list of unique triplets where the sum is zero.
        """
        res = []

        # Sort the input array
        nums.sort()

        for i in range(len(nums) - 2):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer approach
            j, k = i + 1, len(nums) - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    # Found a valid triplet
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates for the second and third numbers
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif three_sum > 0:
                    k -= 1
                else:
                    j += 1

        return res

# Detailed Time Complexity:
# - Sorting the array takes O(n log n).
# - The outer loop iterates n times in the worst case.
# - For each iteration of the outer loop, the two-pointer approach takes O(n) time.
# - Thus, the total time complexity is O(n^2).

# Detailed Space Complexity:
# - The algorithm uses O(1) additional space for the two-pointer technique since it modifies the array in-place for sorting.
# - The result list is not included in the space complexity analysis.

