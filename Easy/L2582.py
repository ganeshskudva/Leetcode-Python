class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        def is_even(n):
            return n % 2 == 0

        chunks = time // (n - 1)
        return time % (n - 1) + 1 if is_even(chunks) else n - time % (n - 1)
