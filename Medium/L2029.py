class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        # Count occurrences of stones based on modulo 3
        mod = [0] * 3
        for num in stones:
            mod[num % 3] += 1

        # Early base case check
        if mod[0] % 2 == 0:
            return mod[1] > 0 and mod[2] > 0
        else:
            return abs(mod[1] - mod[2]) > 2
