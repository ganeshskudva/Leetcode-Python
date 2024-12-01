class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, mx = 0, 0  # Initialize count 'cnt' for consecutive 1s and 'mx' to track the maximum

        for n in nums:  # Iterate through the list of numbers
            if n == 1:  # If the current number is 1
                cnt += 1  # Increment the count of consecutive 1s
            else:  # If the current number is 0
                mx = max(mx, cnt)  # Update the maximum with the current count of consecutive 1s
                cnt = 0  # Reset the count to 0 since the sequence of 1s is broken

        return max(mx, cnt)  # Ensure to check the last sequence of 1s after the loop ends

# Time Complexity (TC):
# 1. Iterating through the array: O(n), where n is the length of the array.
#    - Each element in the array is processed exactly once.
# 2. The operations inside the loop (comparison, increment, and assignment) are O(1) for each element.
# Overall TC: O(n).

# Space Complexity (SC):
# 1. The algorithm uses a constant amount of extra space:
#    - Two integer variables `cnt` and `mx` are used to track the current count of 1s and the maximum count.
# 2. No additional data structures are required.
# Overall SC: O(1).
