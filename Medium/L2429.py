class Solution:
    def minimizeXor(self, num1, num2):
        # Count the number of set bits (1s) in num1 and num2
        a, b = num1.bit_count(), num2.bit_count()
        # Initialize the result with num1
        res = num1
        # Iterate over the 32 possible bit positions for a 32-bit integer
        for i in range(32):
            # If the number of set bits in `res` is greater than `num2`, reduce it
            if a > b and (1 << i) & num1 > 0:
                res ^= 1 << i  # Toggle the i-th bit in `res` from 1 to 0
                a -= 1        # Decrease the count of set bits
            # If the number of set bits in `res` is less than `num2`, increase it
            if a < b and (1 << i) & num1 == 0:
                res ^= 1 << i  # Toggle the i-th bit in `res` from 0 to 1
                a += 1        # Increase the count of set bits
        # Return the minimized XOR result
        return res

# Time Complexity (TC): O(32) -> The loop runs at most 32 iterations (constant time).
# Space Complexity (SC): O(1) -> The solution uses a constant amount of extra space.
