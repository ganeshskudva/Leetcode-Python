class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res, self.tmp = [], []
        
        if not nums:
            return self.res
        
        def solve(start):
            self.res.append(list(self.tmp))
            for i in range(start, len(nums)):
                if i and i > start and nums[i] == nums[i - 1]:
                    continue
                self.tmp.append(nums[i])
                solve(i + 1)
                self.tmp = self.tmp[:-1]
        
        nums.sort()
        solve(0)
        
        return self.res
