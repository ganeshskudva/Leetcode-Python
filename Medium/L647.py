class Solution:
    def countSubstrings(self, s: str) -> int:
        # Function to expand around the center and return the count of palindromic substrings
        def expand_from_center(left: int, right: int) -> int:
            count = 0
            # Expand outwards while characters are equal and within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1  # Count this palindromic substring
                left -= 1
                right += 1
            return count

        # Initialize a counter for total palindromic substrings
        cnt = 0
        
        # Iterate over each character as the center for potential palindromes
        for i in range(len(s)):
            # Count palindromic substrings with odd lengths (single center character)
            cnt += expand_from_center(i, i)
            # Count palindromic substrings with even lengths (two center characters)
            cnt += expand_from_center(i, i + 1)
        
        # Return the total count of palindromic substrings
        return cnt

# Time Complexity (TC):
# - Each expansion from the center can take up to O(N) in the worst case.
# - Since we do this expansion twice for each character, the time complexity is O(N^2).

# Space Complexity (SC):
# - We use O(1) additional space as we only use a counter and pointers.
# - Overall space complexity is O(1).
