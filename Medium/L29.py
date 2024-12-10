class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge case for overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Clamp to 32-bit signed integer range
        
        # Determine the sign of the result
        positive = (dividend < 0) == (divisor < 0)
        
        # Work with absolute values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        # Use bit manipulation for efficiency
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        # Apply the sign to the result
        result = result if positive else -result
        
        # Clamp the result to the 32-bit signed integer range
        return max(-2**31, min(result, 2**31 - 1))

# Time Complexity (TC):
# The outer loop iterates while `dividend >= divisor`, effectively reducing the dividend exponentially
# by doubling the divisor (via `temp <<= 1`). This results in O(log(dividend)).
# The inner loop uses bit-shifting, which is a constant-time operation.
# Overall, the time complexity is **O(log(dividend))**.

# Space Complexity (SC):
# The space complexity is **O(1)** because the algorithm only uses a few variables (e.g., `temp`, `multiple`, and `result`).
