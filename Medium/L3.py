from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If the string is empty or has only one character, return its length (0 or 1)
        if len(s) <= 1:
            return len(s)
        
        # Initialize two pointers and a dictionary to store character positions
        left = 0  # Left pointer represents the start of the sliding window
        max_len = 0  # Variable to store the maximum length of a unique substring
        mp = defaultdict(int)  # Dictionary to store the most recent index of each character

        # Traverse the string with the 'right' pointer
        for right in range(len(s)):
            # If the current character has been seen before and is within the current window (i.e., left <= mp[s[right]])
            if s[right] in mp and left <= mp[s[right]]:
                # Move the left pointer to the right of the last occurrence of the current character
                left = mp[s[right]] + 1
            
            # Update the most recent index of the current character in the dictionary
            mp[s[right]] = right

            # Calculate the length of the current window and update max_len if it's the longest so far
            max_len = max(max_len, right - left + 1)

        return max_len

# Time Complexity (TC): O(n), where n is the length of the string 's'.
# Each character is processed at most twice: once by the right pointer and once by the left pointer when adjusting the window.

# Space Complexity (SC): O(min(n, m)), where n is the length of the string and m is the size of the character set.
# The dictionary `mp` stores up to m characters in the worst case, but typically it’s proportional to the length of the substring.
