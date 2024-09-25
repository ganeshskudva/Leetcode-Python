class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, mx = 0, float('-inf')  # Initialize count 'cnt' for consecutive 1s and 'mx' to track the maximum, set to negative infinity initially

        for n in nums:  # Iterate through the list of numbers
            if not n:  # If the current number is 0
                mx = max(mx, cnt)  # Update the maximum with the current count of consecutive 1s
                cnt = 0  # Reset the count to 0 since the sequence of 1s is broken
            else:  # If the current number is 1
                cnt += 1  # Increment the count of consecutive 1s
        
        mx = max(mx, cnt)  # Ensure to check the last sequence of 1s after the loop ends
        return 0 if mx == float('-inf') else mx  # If no 1s were found, return 0, otherwise return the maximum count of consecutive 1s
