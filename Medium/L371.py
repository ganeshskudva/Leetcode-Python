class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xffffffff

        while b & mask:
            c = a & b
            a = a ^ b
            b = c << 1

        return a & mask if b > 0 else a
