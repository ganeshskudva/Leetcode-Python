class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        line = [0] * (n + 1)  # Array to track cumulative shifts

        # Apply the shifts
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                line[start] += 1
                line[end + 1] -= 1
            else:  # Backward shift
                line[start] -= 1
                line[end + 1] += 1

        # Compute the prefix sum to determine final shifts for each character
        for i in range(1, n + 1):
            line[i] += line[i - 1]

        # Apply the shifts to the string
        shifted = []
        for i in range(n):
            # Calculate the new character after applying the shift
            increase_by = (ord(s[i]) - ord('a') + line[i]) % 26
            # Ensure the result is positive
            new_char = chr(ord('a') + (increase_by + 26) % 26)
            shifted.append(new_char)

        return ''.join(shifted)

# Time Complexity (TC):
# O(n + k):
# - O(k) to process all shift operations and update the `line` array, where k is the number of shift operations.
# - O(n) to compute the prefix sum for the `line` array, where n is the length of the string `s`.
# - O(n) to construct the resulting shifted string.

# Space Complexity (SC):
# O(n):
# - The `line` array uses O(n) space to store cumulative shifts.
# - The `shifted` list temporarily stores the shifted string, which also requires O(n) space.
# - No additional data structures are used, so the total space complexity is O(n).
