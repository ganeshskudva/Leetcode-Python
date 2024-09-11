class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        value = start ^ goal
        count = 0
        while value:
            value &= value - 1
            count += 1
        return count
