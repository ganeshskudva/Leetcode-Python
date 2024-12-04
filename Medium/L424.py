from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize the sliding window start, dictionary to count characters, and max count of any character
        left, max_cnt, max_size = 0, 0, 0
        char_count = defaultdict(int)  # Stores the frequency of characters in the current window

        # Iterate through the string with 'right' as the right pointer of the sliding window
        for right, ch in enumerate(s):
            char_count[ch] += 1  # Add the current character to the frequency dictionary
            max_cnt = max(max_cnt, char_count[ch])  # Update max_cnt to reflect the most frequent character

            # If the current window size minus the max count of any character is greater than k, shrink the window
            if right - left + 1 - max_cnt > k:
                char_count[s[left]] -= 1  # Remove the character at the left boundary of the window
                left += 1  # Move the left boundary to the right

            # Update max_size with the size of the current valid window
            max_size = max(max_size, right - left + 1)

        return max_size

# Time Complexity (TC):
# 1. The loop runs for all characters in the string `s`, so it is O(n), where n is the length of `s`.
# 2. Each operation inside the loop (updating `char_count`, calculating `max_cnt`, etc.) is O(1).
# 3. The sliding window ensures each character is added and removed from the `char_count` dictionary at most once.
# Overall, the time complexity is O(n).

# Space Complexity (SC):
# 1. The `char_count` dictionary stores the frequency of characters in the current window.
#    - The number of keys is bounded by the size of the character set, which is O(1) for English alphabet (26 letters).
# 2. No other auxiliary space grows with the size of input.
# Overall, the space complexity is O(1).

