class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Step 1: Find the least significant set bit (k & -k)
        # This operation takes constant time O(1)
        least_significant_bit = k & -k
        
        # Step 2: Divide k by the least significant set bit using integer division
        # Integer division takes constant time O(1)
        divided_value = k // least_significant_bit
        
        # Step 3: Right shift the divided value by 1 and bitwise AND it with 1
        # Right shift and bitwise AND operations are constant time O(1)
        shifted_value = (divided_value >> 1) & 1
        
        # Step 4: XOR the result with the last bit of k
        # XOR and bitwise AND operations are constant time O(1)
        result = shifted_value ^ (k & 1)
        
        # Step 5: XOR the result with 1
        # Final XOR operation is constant time O(1)
        return str(result ^ 1)

# Time Complexity (TC): O(1)
# All bitwise and arithmetic operations in the function are constant time, 
# so the overall time complexity is O(1).

# Space Complexity (SC): O(1)
# The function uses a constant amount of extra space for the intermediate variables,
# so the space complexity is O(1).
