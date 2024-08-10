class Solution:
    def numSquares(self, n: int) -> int:
        mp = defaultdict(int)

        @cache
        def count(num):
            if num == 0:
                return num

            if num in mp:
                return mp[num]

            mx, i = float('inf'), 1
            while i*i <= num:
                mx = min(mx, count(num - (i * i)) + 1)
                i += 1

            mp[n] = mx
            return mp[n]

        return count(n)
