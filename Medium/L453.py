from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Calculate the minimum element in nums
        min_num = min(nums)
        
        # Calculate the total sum of nums
        total_sum = sum(nums)
        
        # The minimum moves required is the total difference between all elements and the minimum element
        # For each element in nums, we calculate how many steps it takes to reduce it to min_num
        # This total difference is equivalent to total_sum - (len(nums) * min_num)
        return total_sum - len(nums) * min_num

# Time Complexity (TC):
# - Calculating `min(nums)` takes O(N), where N is the length of `nums`.
# - Calculating `sum(nums)` also takes O(N).
# - Final calculation `total_sum - len(nums) * min_num` is O(1).
# - Overall time complexity: O(N) due to the two O(N) operations (min and sum).

# Space Complexity (SC):
# - We use a constant amount of additional space (for min_num and total_sum variables),
#   so the space complexity is O(1).
