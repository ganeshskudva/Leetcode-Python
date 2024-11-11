# iterative
class Solution:
    def myPow(self, x, n):
        # Handle negative exponent by converting to positive and taking reciprocal
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        current_product = x

        # Iterate while n > 0
        while n > 0:
            # If n is odd, multiply the result by the current product
            if n % 2 == 1:
                result *= current_product
            # Square the current product to account for halving `n`
            current_product *= current_product
            # Halve `n` by shifting it right (equivalent to `n // 2`)
            n //= 2

        return result

# Time Complexity (TC): O(log n)
# - Each iteration of the loop halves `n`, so the loop runs in O(log n) time.

# Space Complexity (SC): O(1)
# - Only a fixed amount of extra space is used, as we eliminated the recursion stack.


# recursive
class Solution:
    def myPow(self, x, n):
        # Base case: if exponent `n` is zero, return 1 (as x^0 = 1)
        if not n:
            return 1
        # If exponent `n` is negative, compute positive exponent and take reciprocal
        if n < 0:
            return 1 / self.myPow(x, -n)
        # If exponent `n` is odd, reduce `n` by 1 to make it even, multiply result by `x`
        if n % 2:
            return x * self.myPow(x, n - 1)
        # If exponent `n` is even, square `x` and halve `n` for faster calculation
        return self.myPow(x * x, n // 2)

# Time Complexity (TC): O(log n)
# - The function splits the exponent `n` in half for each recursive call (when `n` is even),
#   reducing the exponent size logarithmically, making the time complexity O(log n).

# Space Complexity (SC): O(log n)
# - The recursion depth is proportional to the number of times we can halve `n`, 
#   which is O(log n) recursive calls in total.

