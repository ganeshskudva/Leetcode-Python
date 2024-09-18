class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize the sliding window start, dictionary to count characters, and max count of any character
        start, max_cnt, max_size = 0, 0, 0
        char_count = defaultdict(int)  # Stores the frequency of characters in the current window

        # Iterate through the string with 'end' as the right pointer of the sliding window
        for end in range(len(s)):
            char_count[s[end]] += 1  # Add the current character to the frequency dictionary
            max_cnt = max(max_cnt, char_count[s[end]])  # Update max_cnt to reflect the most frequent character

            # If the current window size minus the max count of any character is greater than k, shrink the window
            if end - start + 1 - max_cnt > k:
                char_count[s[start]] -= 1  # Remove the character at the left boundary of the window
                start += 1  # Move the left boundary to the right

            # Update max_size with the size of the current valid window
            max_size = max(max_size, end - start + 1)

        return max_size
