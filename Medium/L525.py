class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Find the maximum length of a contiguous subarray with an equal number of 0s and 1s.

        :param nums: List[int] - Input array of binary numbers (0s and 1s).
        :return: int - Maximum length of the contiguous subarray.
        """
        res, zero, one = 0, 0, 0  # Initialize result and counters for zeros and ones
        mp = {0: -1}  # HashMap to store the first occurrence of a particular difference (zero-one count)

        # Iterate through the binary array
        for i, n in enumerate(nums):
            # Update counters for zeros and ones
            if n:
                one += 1
            else:
                zero += 1
            
            # Calculate the difference between the counts of zeros and ones
            diff = zero - one
            
            # Check if the same difference has been seen before
            if diff in mp:
                # Calculate the length of the subarray and update the result if it's the maximum so far
                res = max(res, i - mp[diff])
            else:
                # Store the first occurrence of the difference
                mp[diff] = i

        return res

# Time Complexity (TC): O(n)
# - We traverse the input array once, and hash map operations (insertion and lookup) are O(1) on average.
# - Hence, the time complexity is O(n).

# Space Complexity (SC): O(n)
# - The hash map can store up to n unique differences in the worst case.
# - Therefore, the space complexity is O(n).
