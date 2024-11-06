class Solution:
    def myPow(self, x, n):
        # Base case: if n is 0, return 1 as anything raised to power 0 is 1
        if not n:
            return 1
        # If n is negative, compute the reciprocal of x to convert n to positive
        if n < 0:
            return 1 / self.myPow(x, -n)
        # If n is odd, multiply x once and reduce n by 1 to make it even
        if n % 2:
            return x * self.myPow(x, n - 1)
        # If n is even, compute x * x and reduce the power by half
        return self.myPow(x * x, n / 2)

        # TC: O(log n), as the function halves n in each recursive call, resulting in a logarithmic depth.
        # SC: O(log n), due to the recursion stack, which holds log n calls for positive n.
