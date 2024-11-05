class Solution:
    def minOperations(self, s: str) -> int:
        swaps = 0  # Counter for swaps needed to match Pattern 1 (010101...)
        
        # Iterate over each character in the string
        for i, ch in enumerate(s):
            if i % 2 == 0:
                # If index is even, Pattern 1 expects '0'
                if ch != '0':
                    swaps += 1
            else:
                # If index is odd, Pattern 1 expects '1'
                if ch != '1':
                    swaps += 1
        
        # Return the minimum swaps between Pattern 1 (swaps) and Pattern 2 (len(s) - swaps)
        return min(swaps, len(s) - swaps)

# Time Complexity (TC): O(n), where n is the length of the string `s`.
# - We iterate over each character in `s` once, making this operation linear in time.

# Space Complexity (SC): O(1), as we only use a few variables (such as `swaps`) to store intermediate results.
# - No additional space is required that grows with the input size.
