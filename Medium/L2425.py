class Solution:
    def xorAllNums(self, A, B):
        x = y = 0  # Initialize XOR accumulators for A and B
        
        # Calculate XOR of all elements in A
        for a in A:  # TC: O(len(A)), iterates over all elements in A
            x ^= a
        
        # Calculate XOR of all elements in B
        for b in B:  # TC: O(len(B)), iterates over all elements in B
            y ^= b
        
        # Compute the result based on the parity of the lengths of A and B
        # len(A) % 2 determines if the length of A is odd (1) or even (0)
        # len(B) % 2 determines if the length of B is odd (1) or even (0)
        return (len(A) % 2 * y) ^ (len(B) % 2 * x)  # TC: O(1), single operation

# Overall time complexity: O(len(A) + len(B)) 
# - due to the need to iterate through both arrays.

# Space complexity: O(1) 
# - because we use only a constant amount of extra space (variables `x` and `y`).
