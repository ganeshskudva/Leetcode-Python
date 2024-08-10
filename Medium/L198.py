class Solution:
    def rob(self, nums: List[int]) -> int:
        mp = {}

        def solve(n):
            if n >= len(nums):
                return 0
            if n in mp:
                return mp[n]

            take = nums[n] + solve(n + 2)
            dontTake = solve(n + 1)
            mp[n] = max(take, dontTake)

            return mp[n]

        return solve(0)
