from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Edge case: if k is 0, we cannot have any valid substrings.
        if k == 0:
            return 0

        # Dictionary to track the frequency of characters in the current window.
        count = defaultdict(int)
        
        # Initialize variables
        i, res = 0, 0
        
        # Iterate through the string using the right pointer 'j'
        for j in range(len(s)):
            # Add the current character s[j] to the window and update its frequency.
            count[s[j]] += 1
            
            # If the number of distinct characters exceeds k, shrink the window from the left.
            while len(count) > k:
                count[s[i]] -= 1
                # If the frequency of s[i] becomes zero, remove it from the dictionary.
                if count[s[i]] == 0:
                    del count[s[i]]
                # Move the left pointer to the right.
                i += 1
            
            # Update the result with the maximum window size found so far.
            res = max(res, j - i + 1)
        
        # Return the length of the longest substring with at most k distinct characters.
        return res