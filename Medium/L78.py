class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not len(nums):
            return res

        def solve(start, tmp):
            res.append(list(tmp))

            for i in range(start, len(nums)):
                tmp.append(nums[i])
                solve(i + 1, tmp)
                del (tmp[-1])

        solve(0, [])
        return res
