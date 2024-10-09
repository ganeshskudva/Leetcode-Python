class Solution:
    def minimumLength(self, s: str) -> int:
        # Initialize two pointers: 'left' starts at the beginning, 'right' starts at the end of the string
        left, right = 0, len(s) - 1
        
        # Continue as long as the characters at 'left' and 'right' are equal and pointers haven't crossed
        while left < right and s[left] == s[right]:
            # Store the current character to compare
            ch = s[left]
            
            # Move the 'left' pointer towards the middle as long as characters match 'ch'
            while left < right and s[left] == ch:
                left += 1
            
            # Move the 'right' pointer towards the middle as long as characters match 'ch'
            while left < right and s[right] == ch:
                right -= 1
        
        # If after the loop, the 'left' and 'right' pointers are at the same character, return 0 (all characters are removed)
        # Otherwise, return the length of the remaining valid substring (right - left + 1)
        return 0 if s[left] == ch else right - left + 1

# Time Complexity (TC):
# - The algorithm uses two pointers, each of which traverses the string once. 
# - In each step, either the left pointer moves towards the center or the right pointer does, and each movement is a constant-time operation.
# - Therefore, the overall time complexity is O(n), where `n` is the length of the string `s`.

# Space Complexity (SC):
# - The algorithm only uses a few integer variables (`left`, `right`, `ch`) that do not depend on the size of the input.
# - Thus, the space complexity is O(1), as the extra space used remains constant irrespective of the input size.
