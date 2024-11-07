class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Initialize the answer variable to store the maximum count of candidates
        # that have a set bit at a specific position.
        ans = 0
        
        # Loop through each bit position (0 to 31 for 32-bit integers).
        for i in range(32):
            # Count the number of candidates that have the i-th bit set.
            cnt = sum(1 for candidate in candidates if candidate & (1 << i))
            # Update the answer with the maximum count found for any bit position.
            ans = max(ans, cnt)
        
        # Return the maximum number of candidates that share a common bit position.
        return ans

# Time Complexity (TC): O(32 * n) where n is the length of the candidates list.
# - We iterate over 32 bit positions and, for each bit position, check all candidates.
# - This results in an O(n) check for each of the 32 positions, leading to O(32 * n) or simply O(n).

# Space Complexity (SC): O(1)
# - We use only a constant amount of extra space for variables `ans` and `cnt`.
# - There is no additional data structure used that grows with input size.
