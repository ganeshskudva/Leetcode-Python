class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones, n = sum(nums), len(nums)
        x, onesInWindow = 0, 0
        for i in range(n):
            if i >= ones and nums[i - ones]: 
                x -= 1
            if nums[i] == 1: 
                x += 1
            onesInWindow = max(x, onesInWindow)
        return ones - onesInWindow
