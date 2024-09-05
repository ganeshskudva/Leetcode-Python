class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m, res = len(rolls), [0] * n
        x = (mean * (m + n)) - sum(rolls)

        if x <= 0 or (n * 6) < x or 0 == x // n:
            return []

        p, q = divmod(x, n)
        for i in range(n):
            res[i] = p + (1 if q > 0 else 0)
            q -= 1

        return res
