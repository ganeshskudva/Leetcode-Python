class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Decrement n by 1, we will be using the bits of this modified n
        n -= 1
        
        # Initialize b as 1, which will be used as a bitmask
        b = 1
        
        # Iterate over 64 bits, as we're considering typical 64-bit integers
        for i in range(64):
            # Check if the current bit in x (using bitwise AND with b) is 0
            if b & x == 0:
                # If it is 0, update x to set this bit if the corresponding bit in n is 1
                x |= (n & 1) * b
                # Shift n one bit to the right to prepare the next bit for processing
                n >>= 1
            # Shift b one bit to the left for the next bit position
            b <<= 1
        
        # Return the modified x, which now meets the required conditions
        return x

# Time Complexity (TC): O(1) because the loop runs a fixed 64 times, regardless of the values of n or x.
# Space Complexity (SC): O(1) as we use a constant amount of extra space for variables.
