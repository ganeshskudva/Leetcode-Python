class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        for i in range(n):
            num = abs(nums[i])
            if num > n:
                continue
            num -= 1
            if nums[num] > 0:
                nums[num] *= -1
        
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        
        return n + 1
