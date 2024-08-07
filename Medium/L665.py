class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt, n = 0, len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if cnt or (1 < i < n - 1 and nums[i - 2] > nums[i] and nums[i + 1] < nums[i - 1]):
                    return False
                cnt += 1
        return True
