class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Find the maximum value in the list 'nums'
        # Initialize 'length' to 1, which will store the length of the longest subarray of maximum elements
        mx, length = max(nums), 1

        # 'tmp_len' will track the current length of a subarray of elements equal to 'mx'
        tmp_len = 0
        for n in nums:
            if n == mx:
                # If the current element is the maximum, increase the temporary length
                tmp_len += 1
            else:
                # If the current element is not the maximum, update 'length'
                # to the maximum of 'length' and the current 'tmp_len', then reset 'tmp_len'
                length = max(length, tmp_len)
                tmp_len = 0
        
        # After the loop, ensure that if the longest subarray is at the end,
        # 'length' is updated accordingly
        length = max(length, tmp_len)

        # Return the final longest length of the subarray containing the maximum element
        return length