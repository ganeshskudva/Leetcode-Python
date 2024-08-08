class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = [n for n in nums if n % 3 == 0 and n % 2 == 0]
        return sum(res) // len(res) if len(res) else 0
