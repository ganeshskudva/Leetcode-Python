class Solution:
    def canChange(self, s: str, t: str) -> bool:
        """
        Checks if string `s` can be transformed into string `t` by shifting characters
        'L' and 'R' while adhering to the rules.

        Parameters:
        s (str): Source string containing 'L', 'R', and '_'.
        t (str): Target string containing 'L', 'R', and '_'.

        Returns:
        bool: True if transformation is possible, False otherwise.
        """
        n = len(s)
        i, j = 0, 0

        while i < n or j < n:
            # Skip all underscores in `s`
            while i < n and s[i] == '_':
                i += 1
            # Skip all underscores in `t`
            while j < n and t[j] == '_':
                j += 1

            # If either pointer reaches the end or characters mismatch, break
            if i == n or j == n or s[i] != t[j]:
                break

            # Check for invalid moves:
            # 'L' cannot move right, and 'R' cannot move left
            if (s[i] == 'L' and i < j) or (s[i] == 'R' and i > j):
                return False

            # Move to the next character
            i += 1
            j += 1

        # Both strings must be fully processed
        return i == n and j == n


# Time Complexity (TC):
# 1. The function iterates through the characters of `s` and `t` using two pointers, `i` and `j`.
# 2. Each pointer processes each character of the strings exactly once, skipping over underscores ('_').
# 3. The comparison and checks for valid moves are O(1) operations.
# Overall, the time complexity is O(n), where n is the length of the strings.

# Space Complexity (SC):
# 1. The function uses a constant amount of space for variables (`i`, `j`, and auxiliary values).
# 2. No additional data structures or recursive calls are used.
# Overall, the space complexity is O(1).
