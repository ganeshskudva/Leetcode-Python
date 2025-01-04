class Solution:
    def countPalindromicSubsequence(self, input_string: str) -> int:
        from collections import defaultdict

        # Dictionaries to store the minimum and maximum occurrences of each character
        min_exist = {chr(i): float('inf') for i in range(97, 123)}
        max_exist = {chr(i): float('-inf') for i in range(97, 123)}

        # Populate min_exist and max_exist dictionaries
        for i, char in enumerate(input_string):
            min_exist[char] = min(min_exist[char], i)
            max_exist[char] = max(max_exist[char], i)

        # Variable to store the final count of unique palindromic subsequences
        unique_count = 0

        # Iterate over each character in the alphabet
        for char in min_exist:
            # Skip characters that don't appear in the string
            if min_exist[char] == float('inf') or max_exist[char] == float('-inf'):
                continue

            # Use a set to track unique characters between the occurrences
            unique_chars_between = set(input_string[min_exist[char] + 1:max_exist[char]])

            # Add the count of unique characters to the final count
            unique_count += len(unique_chars_between)

        return unique_count

# Time Complexity (TC):
# O(n + 26 * m), where:
#   - O(n) for iterating over the input string to populate `min_exist` and `max_exist`.
#   - O(26 * m) for iterating over 26 characters (fixed size) and extracting unique characters between their min and max indices.
#   - m is the average size of the substring for each character, bounded by n.
# Simplifies to O(n) for practical purposes since 26 is constant.

# Space Complexity (SC):
# O(26 + u), where:
#   - O(26) for storing `min_exist` and `max_exist` dictionaries.
#   - O(u) for the set `unique_chars_between`, where u is the size of the unique characters in the substring.
# Simplifies to O(n) in the worst case if all characters in the string are unique.
