class Solution:
    def longestPalindrome(self, s: str) -> str:
        lo, max_len = 0, 0  # Initialize starting position and maximum length of the longest palindrome found.
        n = len(s)  # Length of the input string.

        # If the string length is less than 2, the string itself is the longest palindrome.
        if n < 2:
            return s

        # Helper function to check if characters at `left` and `right` match and are within bounds.
        def is_match(left: int, right: int) -> bool:
            # Checks if `left` and `right` are valid indices and characters at these indices are the same.
            return left >= 0 and right < n and s[left] == s[right]

        # Function to expand around the center and update the longest palindrome's position and length.
        def extend_pal(left: int, right: int, low: int, mx_len: int):
            # Expand outwards as long as `left` and `right` are within bounds and characters match.
            while is_match(left, right):
                left, right = left - 1, right + 1

            # Calculate the current palindrome length after expansion stops.
            current_len = right - left - 1
            # Update `low` and `mx_len` if the current palindrome is longer than previously recorded.
            if mx_len < current_len:
                low = left + 1
                mx_len = current_len
            return low, mx_len

        # Iterate through each character to consider it as a potential center of a palindrome.
        for i in range(n):
            lo, max_len = extend_pal(i, i, lo, max_len)       # Odd-length palindromes
            lo, max_len = extend_pal(i, i + 1, lo, max_len)   # Even-length palindromes

        # Return the longest palindromic substring found.
        return s[lo:lo + max_len]

# Time Complexity (TC):
# O(n^2), where n is the length of the string.
# - The outer `for` loop iterates over each character in the string, giving O(n) iterations.
# - For each character, `extend_pal` is called twice (once for odd-length and once for even-length palindromes).
# - `extend_pal` can expand up to the boundaries of the string in the worst case, which is O(n) per call.
# - Therefore, the worst-case time complexity is O(n) * O(n) = O(n^2).

# Space Complexity (SC):
# O(1), as the algorithm uses a constant amount of additional space.
# - Only a fixed number of variables (`lo`, `max_len`, `n`, `low`, `mx_len`, `left`, `right`, and `current_len`) are used,
#   regardless of the input size.
# - The function does not use any data structures that grow with the size of the input, so the space complexity is O(1).
