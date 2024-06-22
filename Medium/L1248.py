class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        j = odd = cnt = tot = 0

        def is_odd(n):
            return n % 2 > 0

        for i in range(len(nums)):
            if is_odd(nums[i]):
                odd += 1
                if odd >= k:
                    cnt = 1
                    while not is_odd(nums[j]):
                        cnt, j = cnt + 1, j + 1
                    tot, j = tot + cnt, j + 1
            elif odd >= k:
                tot += cnt

        return tot
