class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot, i = sum(chalk), 0
        num_times = k // tot
        k = k - (num_times * tot)
        if not k:
            return 0

        while k:
            if chalk[i] > k:
                break
            k -= chalk[i]
            i = (i + 1) % len(chalk)

        return i
