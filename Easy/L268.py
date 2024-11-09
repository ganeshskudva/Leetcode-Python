from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate the sum of elements in the nums array
        total, n = sum(nums), len(nums)
        
        # Calculate the expected sum of numbers from 0 to n using the formula n * (n + 1) / 2
        curr = (n * (n + 1)) // 2
        
        # The difference between curr and total gives the missing number
        return abs(total - curr)

# Time Complexity (TC): O(n)
# - Calculating sum(nums) takes O(n) time, where n is the length of the array.
# - The other operations (calculating curr and returning the result) are O(1).
# - Therefore, the overall time complexity is O(n).

# Space Complexity (SC): O(1)
# - The function uses a constant amount of extra space for variables total, n, and curr.
# - Thus, the space complexity is O(1).
