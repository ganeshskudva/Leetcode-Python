class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Dictionary to store the frequency of characters in the current sliding window.
        mp = defaultdict(int)
        
        # Initialize two pointers, 'left' for the left boundary of the window, and 'right' for the right boundary.
        # max_len will keep track of the maximum length of valid substrings found.
        left, max_len = 0, 0

        # Iterate through the string with 'right' as the right pointer for the sliding window.
        for right in range(len(s)):
            # Add the current character s[right] to the sliding window and update its frequency.
            mp[s[right]] += 1

            # If the number of distinct characters exceeds 2, shrink the window from the left.
            while len(mp) > 2:
                # Decrease the frequency of the character at s[left] as it's being removed from the window.
                mp[s[left]] -= 1

                # If the frequency of s[left] becomes 0, remove it from the dictionary as it's no longer in the window.
                if mp[s[left]] == 0:
                    del mp[s[left]]

                # Move the left pointer to the right to shrink the window.
                left += 1

            # Update the maximum length of valid substrings with at most two distinct characters.
            max_len = max(max_len, right - left + 1)

        # Return the maximum length of the substring that contains at most two distinct characters.
        return max_len