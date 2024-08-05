class Solution:
    def binaryGap(self, n: int) -> int:
        mx, num = 0, bin(n)
        start = 0
        for i, c in enumerate(num[2:]):
            if c == '1':
                mx = max(mx, i - start)
                start = i

        return mx
